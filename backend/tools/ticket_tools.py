
from backend.services.bigquery_service import BigQueryService



bq = BigQueryService()

def get_urgent_tickets():

    sql = """
   SELECT *
    FROM `soda-hackathon.soda_dataset.gold_ticket_queue`
    WHERE queue_status = 'URGENT'
    """

    return bq.query(sql)


def get_ticket_operations_summary():
     sql = """
     SELECT *
     FROM `soda-hackathon.soda_dataset.gold_ticket_operations`
     ORDER BY open_tickets DESC
    """
     return bq.query(sql)
