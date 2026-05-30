from pydantic import BaseModel
from typing import Optional


class Customer(BaseModel):
    customer_id: str
    full_name: str
    customer_status: str
    region: str
    health_score: float

  