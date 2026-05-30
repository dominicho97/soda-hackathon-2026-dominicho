
import pandas as pd

from backend.schemas.ticket_schema import SupportTicket

#normally I wanted to do this with google sheets but had some issues with authentication

class TicketCsvConnector:

    def fetch_tickets(self) -> list[SupportTicket]:

        df = pd.read_csv(
            "datasets/support_tickets_dataset.csv"
        )

        df = df.rename(columns={
            "Ticket ID": "ticket_id",
            "Customer Email": "customer_email",
            "Ticket Priority": "ticket_priority",
            "Ticket Status": "ticket_status",
            "Ticket Type": "ticket_type"
        })

        return [
            SupportTicket(**row.to_dict())
            for _, row in df.iterrows()
        ]