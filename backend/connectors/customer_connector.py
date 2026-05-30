import os
import psycopg2

from dotenv import load_dotenv

from backend.schemas.customer_schema import Customer

load_dotenv()


class CustomerPostgresConnector:

    def __init__(self):

        self.connection = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )


    def fetch_customers(self):

        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT
                customer_id,
                full_name,
                customer_status,
                region,
                health_score
            FROM customers
        
        """)

        rows = cursor.fetchall()

        customers = []


        

        for row in rows:

            customers.append(
      Customer(
    customer_id=row[0],
    full_name=row[1],
    customer_status=row[2],
    region=row[3],
    health_score=row[4]
)
            )

        return customers
    

   