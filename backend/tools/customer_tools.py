from backend.services.bigquery_service import BigQueryService








bq = BigQueryService()

def get_high_risk_customers():

    sql = """
    SELECT *
    FROM `soda-hackathon.soda_dataset.gold_customer_health`
    WHERE churn_risk = 'HIGH'
    """

    return bq.query(sql)


def get_customer_health_summary():
    sql = """  
    SELECT *
    FROM `soda-hackathon.soda_dataset.gold_customer_health_summary`  """
    return bq.query(sql)