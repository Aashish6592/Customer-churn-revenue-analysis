# Customer-churn-revenue-analysis
Customer churn and revenue retention analysis using SQL, Python, and Power BI.

An end-to-end data analytics project focused on understanding customer churn, identifying key churn drivers, and analyzing revenue at risk.

## Project Overview

Customer churn is a major challenge for subscription-based businesses. This project analyzes customer, subscription, usage, and transaction data to identify patterns associated with customer churn and provide data-driven retention insights.

## Objectives

- Analyze overall customer churn
- Identify major factors associated with churn
- Compare churn across customer segments
- Analyze customer usage and subscription behavior
- Measure revenue lost due to churn
- Identify high-value customers at risk
- Build an interactive Power BI dashboard
- Provide actionable business recommendations

## Tech Stack

- SQL
- PostgreSQL
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Power BI

## Project Workflow

Raw Data  
↓  
Data Cleaning  
↓  
SQL Analysis  
↓  
Exploratory Data Analysis  
↓  
Customer Segmentation  
↓  
Revenue Risk Analysis  
↓  
Power BI Dashboard  
↓  
Business Recommendations

## Project Status

🚧 Currently in development.

## Repository Structure

data/         → Raw and cleaned datasets
sql/          → SQL queries and analysis
python/       → Data cleaning and exploratory analysis
powerbi/      → Power BI dashboard
screenshots/  → Dashboard screenshots

## Data Cleaning & Validation

All 5 datasets were validated for the following:
- Missing/duplicate customer IDs
- Invalid ages, tenure, charges
- Logical consistency (churned status vs churn_date)
- Invalid categorical values (payment methods, statuses)

**Result:** All 12 validation checks passed with 0 anomalies found, confirming data integrity across all tables.
