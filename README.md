# Sentinela

**Sentinela** is a data intelligence tool designed to automate criminal analysis and optimize public safety strategic planning.

Originally conceived during my service at the Military Police of São Paulo (PMESP), this project was born from the need to transform raw, manual data from the SSP-SP (Public Safety Secretariat) into actionable insights, replacing slow, manual reporting with an automated ETL and visualization pipeline.

---

## 🚀 The Context & Motivation
In the public safety sector, data is often handled manually, leading to critical delays. I developed this solution to automate the identification of theft and robbery patterns. Although the automation faced institutional resistance at the time—as it significantly reduced manual labor for statistical sectors—it stands as a testament to my proactive approach to solving real-world problems with high-performance technology.

## 📊 Study Case & Data Source
This project utilizes a **public study database** derived from the [SSP-SP (São Paulo Public Safety Secretariat)](https://www.ssp.sp.gov.br) records for the year 2025. It is intended for **research and educational purposes only**, showcasing how data engineering can be applied to public safety statistics. All data is handled according to transparency principles, focusing on statistical trends.

## 🛠 Tech Stack
*   **Backend:** Python / Flask
*   **Data Science:** Pandas & NumPy
*   **Database:** PostgreSQL (Relational storage for performance)
*   **Infrastructure:** Docker & Docker Compose
*   **Security:** Environment Variables (`.env`) for sensitive credentials

## ⚠️ Project Status: In Development
This is a living project. I am currently migrating legacy analysis scripts into this containerized architecture.

### **Upcoming Features (Roadmap):**
- [ ] **Data Expansion:** Integration of updated monthly databases from SSP-SP (2025 onwards).
- [ ] **Heatmaps:** Dynamic crime mapping using Folium/Leaflet.
- [ ] **Advanced Filters:** Capability to filter by time ranges, vehicle models, and specific neighborhoods.
- [ ] **REST API:** Endpoints to serve JSON data for external dashboards (PowerBI/Tableau).


