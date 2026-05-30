from google.cloud import bigquery
import pandas as pd


class BigQueryLoader:

    def __init__(self):
        self.client = bigquery.Client(
            project="soda-hackathon"
        )

    def load_models(self, models, table_name):

        df = pd.DataFrame(
            [m.model_dump() for m in models]
        )

        table_id = (
            f"soda-hackathon.soda_dataset.{table_name}"
        )

        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE"
        )

        job = self.client.load_table_from_dataframe(
            df,
            table_id,
            job_config=job_config
        )

        job.result()

        print(
            f"Loaded {len(df)} rows into {table_id}"
        )


        # loader = BigQueryLoader()

        # loader.load_models(
        #     tickets,
        #     "support_tickets"
        # )

        # loader.load_models(
        #     customers,
        #     "customers"
        # )