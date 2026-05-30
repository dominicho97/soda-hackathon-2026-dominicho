from backend.tools.customer_tools import get_high_risk_customers
from backend.tools.ticket_tools import get_urgent_tickets

customers = get_high_risk_customers()
tickets = get_urgent_tickets()

print(customers.head())
print(tickets.head())