# Vehicle Insurance Fraud Detection

## Overview
This project implements an end-to-end data engineering pipeline to detect fraudulent vehicle insurance claims using streaming and batch data processing techniques.

## Tech Stack
- Apache Kafka (Streaming ingestion)
- PySpark (Data processing & ML)
- Python
- Power BI (Visualization)
- Decision Tree ML Model

## Architecture
CSV Data → Kafka → PySpark → Feature Engineering → Fraud Detection Model → Power BI Dashboard

## Key Features
- Simulated real-time data ingestion using Kafka
- Large-scale data processing with PySpark
- Fraud detection using Decision Tree model (94%+ precision & recall)
- Interactive Power BI dashboard for fraud trend analysis

## Outcomes
- Identified high-risk claims and fraud patterns
- Visualized claim behavior and policy-level risks
- Demonstrated end-to-end data engineering workflow

## How to Run
1. Start Kafka (optional simulation)
2. Run PySpark preprocessing scripts
3. Train fraud detection model
4. Load processed data into Power BI
