# 20 Days of Data Engineering 🛠️📊

A structured, hands-on journey through the modern Data Engineering tech stack. This repository documents my code, exercises, and learnings as I progress through 20 days of intensive Data Engineering challenges.

## 🚀 About The Challenge

This curriculum moves from foundational scripting and database skills to modern ETL frameworks, big data processing, and orchestration. It is designed to simulate real-world data engineering tasks.

### Core Tech Stack

- **Languages:** Python, SQL, Bash
- **Databases:** PostgreSQL
- **Big Data:** PySpark, Parquet
- **Orchestration:** Apache Airflow
- **Infrastructure:** Docker, Terraform

## 📂 Repository Structure

```
├── 01-foundations/        # Days 1-5: Python, SQL, Docker, Linux
├── 02-etl-pipelines/      # Days 6-10: APIs, Validation, IaC
├── 03-big-data/           # Days 11-15: Spark, Airflow, Cloud Storage
├── 04-advanced/           # Days 16-20: dbt, Kafka, CI/CD, Capstone
├── docker-compose.yml     # Services setup (Postgres, Airflow, etc.)
├── requirements.txt       # Python dependencies
└── README.md
```

## 📅 The Curriculum

### Phase 1: The Foundations (Python, SQL & Systems)

| Day | Topic                    | Key Concept              | Status |
|-----|--------------------------|--------------------------|--------|
| 01  | Iterators & Generators   | Memory efficiency        | [ ]    |
| 02  | SQL Window Functions     | `RANK`, `LEAD`, `LAG`    | [ ]    |
| 03  | Linux & Bash             | Automation scripting     | [ ]    |
| 04  | Docker Fundamentals      | Containerization         | [ ]    |
| 05  | Data Modeling            | Star Schema design       | [ ]    |

### Phase 2: Building ETL Pipelines

| Day | Topic                    | Key Concept              | Status |
|-----|--------------------------|--------------------------|--------|
| 06  | API Extraction           | `requests` & JSON parsing| [ ]    |
| 07  | Data Formats             | Parquet vs CSV           | [ ]    |
| 08  | Batch ETL Script         | Extract, Transform, Load | [ ]    |
| 09  | Data Quality             | Validation with Pydantic | [ ]    |
| 10  | Infrastructure as Code   | Terraform basics         | [ ]    |

### Phase 3: Big Data & Orchestration

| Day | Topic                    | Key Concept              | Status |
|-----|--------------------------|--------------------------|--------|
| 11  | Intro to PySpark         | Distributed processing   | [ ]    |
| 12  | Spark Optimization       | UDFs & Partitioning      | [ ]    |
| 13  | Airflow Basics           | DAGs & Operators         | [ ]    |
| 14  | Orchestrating ETL        | Airflow Hooks            | [ ]    |
| 15  | Cloud Storage            | Mock S3 (Minio/LocalStack)| [ ]   |

### Phase 4: Advanced Topics & Capstone

| Day | Topic                    | Key Concept              | Status |
|-----|--------------------------|--------------------------|--------|
| 16  | Data Warehousing         | dbt (Data Build Tool)    | [ ]    |
| 17  | Streaming Data           | Apache Kafka             | [ ]    |
| 18  | CI/CD for Data           | GitHub Actions           | [ ]    |
| 19  | Reverse ETL              | Operational Analytics    | [ ]    |
| 20  | Capstone Project         | End-to-End Pipeline      | [ ]    |

## 🛠️ How to Run

### Prerequisites

- Docker Desktop installed
- Python 3.9+

### Setup

1. **Clone the repo:**

```bash
git clone https://github.com/bomkazin/20-days-data-engineering.git
cd 20-days-data-engineering
```

2. **Start Infrastructure (Postgres, etc.):**

```bash
docker-compose up -d
```

3. **Install Python
```bash
pip install -r requirements.txt
```