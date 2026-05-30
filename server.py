import mcp.server.transport_security as _ts
_ts.TransportSecurityMiddleware.__init__ = lambda self, settings=None: setattr(
    self, 'settings', _ts.TransportSecuritySettings(enable_dns_rebinding_protection=False)
)

from backend.tools.agent_actions_tools import create_customer_action_plan


from mcp.server.fastmcp import FastMCP
from backend.tools.customer_tools import get_high_risk_customers, get_customer_health_summary
from backend.tools.ticket_tools import get_urgent_tickets, get_ticket_operations_summary
import os

mcp = FastMCP("bigquery-tools")

@mcp.tool()
def high_risk_customers() -> list[dict]:
    """Return all customers with HIGH churn risk."""
    return get_high_risk_customers().to_dict(orient="records")

@mcp.tool()
def customer_health_summary() -> list[dict]:
    """Return the customer health summary."""
    return get_customer_health_summary().to_dict(orient="records")

@mcp.tool()
def urgent_tickets() -> list[dict]:
    """Return all tickets with URGENT queue status."""
    return get_urgent_tickets().to_dict(orient="records")

@mcp.tool()
def ticket_operations_summary() -> list[dict]:
    """Return ticket operations ordered by open tickets descending."""
    return get_ticket_operations_summary().to_dict(orient="records")


@mcp.tool()
def customer_action_plan() -> dict:
    """Generate a customer action plan for all high risk customers."""
    return create_customer_action_plan()

if __name__ == "__main__":
    # mcp.run(transport="streamable-http")
    # mcp.run(transport="streamable-http", host="0.0.0.0", port=8080)
    port = int(os.environ.get("PORT", 8080))
    mcp.settings.host = "0.0.0.0"
    mcp.settings.port = port
    mcp.run(transport="streamable-http")