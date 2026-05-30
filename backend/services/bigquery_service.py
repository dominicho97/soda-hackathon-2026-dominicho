# backend/services/bigquery_service.py

from google.cloud import bigquery

class BigQueryService:

    def __init__(self):
        self.client = bigquery.Client()

    def query(self, sql: str):
        return self.client.query(sql).to_dataframe()