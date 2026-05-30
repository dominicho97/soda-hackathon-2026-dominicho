from pydantic import BaseModel




class Customer(BaseModel):
    customer_id: str
    gender: str
    tenure: int
    contract: str
    churn: str