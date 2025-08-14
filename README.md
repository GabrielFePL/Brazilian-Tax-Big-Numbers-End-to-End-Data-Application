## GitHub Task Board  
Task Board URL: https://github.com/users/GabrielFePL/projects/5/views/1  

## Steps and Architecture  

### 1. Environment Setup  
Preparation and configuration of the development environment, ensuring all required tools and platforms, such as Databricks for data processing and GitHub for version control are properly set up and integrated according to the needs of the data pipeline.

---

### 2. Web Scraping and Data Retrieval  
Implementation of an automated web scraping process to collect datasets from public sources, ensuring the latest available data is always retrieved without manual intervention.  

Key aspects include:  
- Automation: Eliminates repetitive manual downloads, reducing human error.  
- Data Freshness: Always pulls the latest version of each dataset for analysis.  
- Scalability: Easily extendable to multiple data portals or additional datasets.  
- Reproducibility: Guarantees a consistent process for obtaining raw data, crucial for audits and compliance.  

---

### 3. Data Storage in Unity Catalog  
Raw data obtained through scraping is saved as source files in the **Unity Catalog**, and future medallion architecture layers are saved as delta tables, with the following objectives:  
- Centralized storage with secure access control.  
- Integration with Databricks for automated data access.  
- Support for data governance and traceability.  

Data source URL:  
https://dados.gov.br/dados/conjuntos-dados/grandes-nmeros-do-imposto-de-renda-da-pessoa-fsica  

---

### 4. Medallion Architecture  
Implementation of the Medallion architecture in Databricks to ensure:  
- **Bronze**: ingestion of raw data.  
- **Silver**: cleaning, standardization, and enrichment.  
- **Gold**: data ready for analysis and modeling.  
- High scalability, easy maintenance, and historical data retention.  

---

### 5. Star Schema Modeling  
Dimensional modeling focused on analytical performance:  
- **Dimension Tables (dim)**  
- **Fact Table (fact_tax)**  
- Optimized relationships for BI visualizations and analysis.  

---

### 6. Unity Catalog Documentation  
Use of descriptions and tags to:  
- Facilitate understanding and use of the tables.  
- Enable Genie functionality with contextual metadata.  
- Improve data governance and accessibility.  

---

### 7. Genie (Data Assistant)  
Tool integrated with Databricks that allows:  
- Execution of common queries through natural language.  
- Support for frequently asked questions about the data (FAQ).  
- User-friendly interface for business users and analysts.  

---

### 8. Databricks Dashboards Application  
Development of interactive dashboards within Databricks for real-time data visualization and insight generation.  
- These dashboards consume curated data from the Gold layer.  
- Enable dynamic exploration, performance monitoring, and decision-making support through intuitive visual representations.  

---

### 9. Data Ingestion with Databricks Workflows  
Use of **Databricks Job Workflows** for ingesting and transforming data:  
- Orchestrated pipeline to transform raw data into structured data.  
- Scheduled execution.  
- Compatible with the Medallion architecture (bronze, silver, gold).  
