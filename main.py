from backend.connectors.ticket_csv_connector import TicketCsvConnector
from backend.connectors.customer_connector import CustomerPostgresConnector
from bigquery_loader import BigQueryLoader

ticket_connector = TicketCsvConnector()
customer_connector = CustomerPostgresConnector()

tickets = ticket_connector.fetch_tickets()
customers = customer_connector.fetch_customers()

print(f"Tickets: {len(tickets)}")
print(f"Customers: {len(customers)}")

print(tickets[0])
print(customers[0])



