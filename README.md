# soda-hackathon-2026-dominicho


<img width="581" height="329" alt="image" src="https://github.com/user-attachments/assets/bfc397b7-28eb-49ea-a89c-955d9c64413e" />





StrawOps is a governed AI operations platform that transforms raw enterprise data into trusted business actions.

We ingest customer and support data from PostgreSQL and CSV sources, validate it using Pydantic schemas, and load it into BigQuery using a Medallion architecture (Bronze, Silver, Gold). The Silver layer standardizes and enriches data, while the Gold layer creates business-ready entities such as customer health, churn risk, and support ticket prioritization.

Instead of allowing AI agents to query raw databases directly, StrawOps exposes governed business tools through Soda Straw. These tools provide access to trusted business concepts such as high-risk customers, customer health summaries, urgent support tickets, and operational support metrics.

The agent can reason over validated and enriched data to answer business questions, identify risks, and generate operational recommendations. To close the loop, StrawOps demonstrates reverse ETL by automatically generating customer action plans that can be consumed by downstream business systems and teams.

By combining data governance, semantic business layers, and agent-driven automation, StrawOps enables organizations to move from raw data to actionable outcomes while maintaining trust, consistency, and control.
