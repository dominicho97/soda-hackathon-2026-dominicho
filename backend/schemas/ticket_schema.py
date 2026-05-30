from pydantic import BaseModel







class SupportTicket(BaseModel):
    ticket_id: str
    customer_email: str
    ticket_priority: str
    ticket_status: str
    ticket_type: str