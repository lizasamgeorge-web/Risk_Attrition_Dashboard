📑 Project Title: Omnichannel Portfolio Attrition Risk Engine

Technology Stack: Python (Pandas, NumPy), Power BI Desktop, Advanced DAX, Power Query.

1. Situation & Task (The Business Problem)
Traditional proactive retention strategies in retail banking rely heavily on lagging indicators—such as total balance depletion or formal account closure requests. By the time these triggers fire, the customer relationship has already disintegrated, resulting in high attrition costs.

The Challenge: Front-line relationship teams face massive information overload when managing thousands of accounts. They lack a data-driven mechanism to separate harmless "Digital Migration" (customers moving from branches to the mobile app) from true "Silent Churn" (customers quietly moving their core transactional volume to a competitor while leaving their balance intact).

The Objective: Build an end-to-end analytical data pipeline to proactively isolate high-priority retention targets before capital flight occurs.

2. Action (The Technical Pipeline)
Phase A: Backend Risk Engineering (Python)
Developed a scalable synthetic sandbox environment using NumPy (np.random.randint) and anchored reproducibility with np.random.seed(42) to simulate a 50-customer active portfolio.

Engineered a multi-dimensional relational database using Pandas DataFrames to track concurrent customer metrics across three primary vectors: historical inactivity windows, digital platform engagement frequency, and asset volatility.

Programmed a multi-layered logical filtering matrix using vectorized bitwise operators (&) to systematically isolate core anomalies based on an operational risk profile.

Phase B: Frontend Business Intelligence (Power BI)
Ingested the processed backend database into Power BI using robust file-path configurations to support seamless automated refreshes.

Designed an executive-level interactive control console utilizing dynamic Visual-Level Filters to bypass unaggregated summaries and expose raw data structures.

Implemented cross-filtered visuals, a compact account slicer console, and an analytical Constant Threshold Line at the 30-day risk boundary to visually partition active accounts from critical relationship decay.

3. Result (The Strategic Business Value)
96% Noise Reduction: Successfully filtered out 48 false-alarm accounts (digital-first migrations and standard drawdowns), preventing wasted operational hours on cold outreach.

Targeted Capital Preservation: Instantly isolated the exact 2 accounts (Customer 1012 and 1021) displaying absolute silent churn metrics (severe branch inactivity paired with near-zero mobile app logins and fully intact idle capital).

Operational Readiness: Delivered a dynamic, CRM-ready interface enabling local branch managers to execute precision relationship check-ins within seconds.
