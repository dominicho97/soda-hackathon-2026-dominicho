import pandas as pd
from datetime import datetime

from backend.tools.customer_tools import get_high_risk_customers


def create_customer_action_plan():

    customers = get_high_risk_customers()

    df = pd.DataFrame(customers)

    if len(df) == 0:
        return {
            "status": "no_actions_required"
        }

    def get_action(health_score):

        if health_score < 20:
            return "Executive Escalation"

        if health_score < 30:
            return "Customer Success Outreach"

        return "Monitor"

    df["recommended_action"] = (
        df["health_score"].apply(get_action)
    )

    df["priority"] = "HIGH"

    df["owner"] = "Customer Success Team"

    df["created_at"] = datetime.utcnow().isoformat()

    # output_file = "datasets/customer_action_plan.csv"
    output_file = "/tmp/customer_action_plan.csv"

    df.to_csv(
        output_file,
        index=False
    )


    return {
        "status": "success",
        "file": output_file,
        "records": len(df)
    }