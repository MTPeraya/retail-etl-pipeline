# 🧭 Project Plan — Retail Sales ETL Pipeline

## 🎯 Project Objective

Build a **production-style batch ETL pipeline** that ingests raw retail sales data, cleans and enriches it, and loads it into a relational database, using modern data engineering tools and best practices.

---

## 📦 Data Source

* **Dataset:** Global Superstore [Kaggle](https://www.kaggle.com/datasets/anandaramg/global-superstore)
* **Format:** Tab-separated text file
* **Type:** Structured transactional retail data
* **Update Pattern:** Batch (static dataset, simulated daily load)

---

## 🧱 System Architecture (High-Level)

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

All components run in **Docker containers**.

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

### 4️⃣ Orchestration (Next Phase)

**Goal:** Automate and monitor the pipeline

* Define DAG with Airflow
* Schedule batch runs
* Track success/failure
* Enable retries and logs

**Why this matters:**
Manual scripts don’t scale — orchestration does.

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

## 📏 Scope (Important — What We Are NOT Doing)

**In scope:**

* Batch ETL
* Data cleaning
* Schema design
* Dockerized services
* Airflow orchestration

**Out of scope (by design):**

* Machine learning
* Real-time streaming
* Spark / Kafka (future work)
* Cloud deployment (future work)

➡️ This keeps the project **focused and realistic for an intern**.

---

## 📈 Success Criteria (How We Know It Works)

The project is successful if:

* ETL runs end-to-end without errors
* Data is correctly loaded into PostgreSQL
* Schema matches design
* Pipeline can be re-run consistently
* Airflow DAG runs on schedule (later)

---

## 🧠 How You’ll Explain This in an Interview

> “I built a containerized batch ETL pipeline that ingests raw retail sales data, performs data cleaning and enrichment with Pandas, loads it into PostgreSQL, and is orchestrated using Airflow. The focus was on data quality, reproducibility, and production-style workflows.”

That answer alone hits **multiple JD bullets**.

---

## 🗺️ Project Milestones (Clear Roadmap)

1. ✅ Define pipeline plan & scope ← **YOU ARE HERE**
2. ⏳ Implement Extract / Transform / Load
3. ⏳ Dockerize services
4. ⏳ Validate data in PostgreSQL
5. ⏳ Add Airflow orchestration
6. ⏳ Final polish (README + resume)

---

## ✅ Next Step (When You’re Ready)

If you say **“continue”**, we will:
➡️ finalize ETL code cleanly
➡️ then move to **Airflow DAG implementation**

Take a moment to read this plan — it’s your **mental map**.
When ready, say **“continue to ETL finalization”** 🚀
