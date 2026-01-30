import os
import pandas as pd
from flask import Flask, render_template
from sqlalchemy import create_engine, inspect
import traceback

app = Flask(__name__)

# CONFIGURAÇÃO SEGURA: O Flask lê a URL do banco injetada pelo Docker
# Se não encontrar nada, ele não inicia, garantindo que não use credenciais expostas
DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ValueError("ERRO: A variável de ambiente DATABASE_URL não foi definida!")

engine = create_engine(DATABASE_URL)

def setup_database():
    """Verifica se o banco está vazio e popula com o Excel se necessário"""
    inspector = inspect(engine)
    if not inspector.has_table("ocorrencias"):
        print("--- Banco vazio! Iniciando importação do Excel ---")
        try:
            # O caminho 'data/...' deve ser relativo à raiz do projeto no container
            file_path = 'data/VeiculosSubtraidos_2025.xlsx'
            df = pd.read_excel(file_path)
            
            # Padronização de colunas: Maiúsculas e sem espaços para evitar erros no Postgres
            df.columns = [c.strip().replace(' ', '_').upper() for c in df.columns]
            
            # Salva no Postgres (o if_exists='replace' garante uma tabela limpa)
            df.to_sql('ocorrencias', engine, index=False, if_exists='replace')
            print(f"--- Sucesso: {len(df)} linhas importadas! ---")
        except Exception as e:
            print(f"--- Erro crítico na importação: {e} ---")
    else:
        print("--- Tabela 'ocorrencias' já existe. Pronto para uso. ---")

@app.route('/')
def index():
    try:
        # Query SQL com aspas duplas para respeitar as colunas em maiúsculo do Postgres
        query = """
            SELECT * FROM ocorrencias 
            WHERE "CIDADE" IN ('COTIA', 'CARAPICUIBA', 'VARGEM GRANDE PAULISTA')
        """
        df = pd.read_sql(query, engine)

        if df.empty:
            return "<h1>Aviso:</h1><p>Nenhum dado encontrado para os filtros selecionados.</p>"

        # Nomes das colunas conforme padronizado no setup_database
        col_tipo = "DESCR_OCORRENCIA_VEICULO"
        col_cidade = "CIDADE"

        # Cálculos para o Dashboard (usando case-insensitive para garantir captura)
        stats = {
            'total_roubo': len(df[df[col_tipo].str.contains('Roubado', na=False, case=False)]),
            'total_furto': len(df[df[col_tipo].str.contains('Furtado', na=False, case=False)]),
            'cidades': sorted(df[col_cidade].unique().tolist())
        }

        # Gera tabela HTML formatada para o Bootstrap no index.html
        tabela_html = df.head(20).to_html(
            classes='table table-striped table-hover', 
            index=False, 
            justify='left'
        )
        
        return render_template('index.html', stats=stats, tabela=tabela_html)
    
    except Exception:
        # Mostra o erro técnico detalhado apenas durante o desenvolvimento
        error_info = traceback.format_exc()
        return f"<h1>Erro na Consulta SQL</h1><pre>{error_info}</pre>"

if __name__ == '__main__':
    # Executa a carga inicial antes de abrir o servidor
    setup_database()
    # Debug=True é ótimo para desenvolvimento, o Flask reinicia ao salvar o arquivo
    app.run(host='0.0.0.0', port=5000, debug=True)

