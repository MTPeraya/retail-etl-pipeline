# Retail Sales ETL Pipeline

## 🎯 Project Objective

Build a **production-style batch ETL pipeline** that ingests raw retail sales data, cleans and enriches it, and loads it into a relational database, using modern data engineering tools and best practices.

---

## 📦 Data Source

* **Dataset:** Global Superstore -> [Kaggle](https://www.kaggle.com/datasets/anandaramg/global-superstore)
* **Format:** Tab-separated text file
* **Type:** Structured transactional retail data
---

## System Architecture (High-Level)

```text
Raw Data (TXT / TSV)
        ↓
Extract (Python)
        ↓
Transform (Pandas)
        ↓
Load (PostgreSQL)
        ↓
Orchestrate (Airflow)
        ↓
Monitor & Log
```

---

## 🔄 Pipeline Stages (What Each Step Does)

### 1️⃣ Extract

**Goal:** Reliable ingestion of raw data

* Read tab-separated file
* Handle encoding and delimiter issues
* Validate that required columns exist
* Output: Raw Pandas DataFrame

**Why this matters:**
Real-world data is rarely clean or standardized.

---

### 2️⃣ Transform

**Goal:** Clean, enrich, and standardize data

Key operations:

* Drop invalid records (missing `Order ID`)
* Convert string dates to `DATE`
* Normalize column names
* Calculate business metrics (`profit_margin`)
* Add ingestion timestamp
* Select final schema

**Why this matters:**
This is where **data quality and business logic** live.

---

### 3️⃣ Load

**Goal:** Persist clean data into analytics-ready storage

* Load into PostgreSQL
* Use append strategy (batch loading)
* Ensure schema compatibility

**Why this matters:**
Databases are the backbone of analytics and reporting.

---

### 4️⃣ Orchestration

**Goal:** Automate and monitor the pipeline

* Define DAG with Airflow
* Schedule batch runs
* Track success/failure
* Enable retries and logs

**Why this matters:**
Manual scripts don’t scale - orchestration does.

---

## 🐳 Infrastructure & Tooling

| Layer            | Tool       | Purpose                 |
| ---------------- | ---------- | ----------------------- |
| Language         | Python     | ETL logic               |
| Data Processing  | Pandas     | Transformations         |
| Database         | PostgreSQL | Data warehouse          |
| Containerization | Docker     | Reproducibility         |
| Orchestration    | Airflow    | Scheduling & monitoring |

---
