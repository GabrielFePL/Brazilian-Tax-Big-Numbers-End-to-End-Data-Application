# Brazilian Tax Big Numbers End to End Data Application
End-to-end data pipeline using Databricks for Brazilian tax data analysis: automated web scraping, secure data storage in Unity Catalog, ingestion and transformation with Job Workflows, Medallion architecture (bronze/silver/gold), star schema modeling, Genie assistant with natural language queries, and interactive dashboards.

# Architecture

## 1. Environment Setup
Preparation of development environments; tools such as Databricks and GitHub are configured according to the data pipeline.

---

## 2. Data Collection with Web Scraping
Automation of data collection on Brazilian tax big numbers using web scraping techniques.

This step allows:
- Periodic extraction of updated data.
- Continuous pipeline maintenance without manual intervention.
- Scheduled scripts based on the project's periodicity for dynamic data updates.

Resource data url:
[https://dados.gov.br/dados/conjuntos-dados/importacoes-e-exportacoes](https://dados.gov.br/dados/conjuntos-dados/grandes-nmeros-do-imposto-de-renda-da-pessoa-fsica)

---

## 3. Storage in Unity Catalog
Raw data obtained through scraping is saved as source files in the **Unity Catalog**, and future medallion architecture layers are saved as delta tables, with the following objectives:
- Centralized storage with secure access control.
- Integration with Databricks for automated data access.
- Support for data governance and traceability.

---

## 4. Data Ingestion with Databricks Workflows
Use of **Databricks Job Workflows** for ingesting and transforming data:
- Orchestrated pipeline to transform raw data into structured data.
- Scheduled execution.
- Compatible with the Medallion architecture (bronze, silver, gold).

---

## 5. Medallion Architecture
Implementation of the Medallion architecture in Databricks to ensure:
- **Bronze**: ingestion of raw data.
- **Silver**: cleaning, standardization, and enrichment.
- **Gold**: data ready for analysis and modeling.
- High scalability, easy maintenance, and historical data retention.

---

## 6. Star Schema Modeling
Dimensional modeling focused on analytical performance:
- **Dimension Tables (dim)**
- **Fact Table (fact_tax)**
- Optimized relationships for BI visualizations and analysis.

---

## 7. Unity Catalog Documentation
Use of descriptions and tags to:
- Facilitate understanding and use of the tables.
- Enable Genie functionality with contextual metadata.
- Improve data governance and accessibility.

---

## 8. Genie (Data Assistant)
Tool integrated with Databricks that allows:
- Execution of common queries through natural language.
- Support for frequently asked questions about the data (FAQ).
- User-friendly interface for business users and analysts.

---

## 9. Databricks Dashboards Application
- Visualization and generation of insights.

---
