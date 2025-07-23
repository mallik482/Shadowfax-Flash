import json
from mcp.server.fastmcp import FastMCP  # Placeholder import, replace with actual MCP import
import os
import requests

mcp = FastMCP(name="shadowfax-mcp-server")

from dotenv import load_dotenv
load_dotenv()


@mcp.tool()
def add(a, b):
    return a + b

@mcp.tool()
def placeOrder(pickup_address: str, drop_address: str, user_contact: str, items: list[dict]):
    ''' call the shadowfax api to place an order '''
    url = "https://hlbackend.staging.shadowfax.in/api/v2/orders/"
    headers = {
        "Authorization": f"Token {os.getenv('SHADOWFAX_API_KEY')}",
        "Content-Type": "application/json"
    }
    data = {
        "order_items": items,
        "drop_details": {
            "address": drop_address,
            "latitude": 12.927684,
            "city": "Delhi",
            "name": "Ashish Yadav",
            "longitude": 77.609162,
            "contact_number": user_contact
        },
        "order_details": {
            "paid": "true",
            "client_order_id": "72427791891231012",
            "client_surge": 100.0,
            "order_value": 10.0,
            "delivery_instruction": {
                "drop_instruction_text": "Mx Name Roll Point Phone 1 7249485361,Phone 2 9049105574,Phone 3 8830254804,",
                "take_drop_off_picture": True,
                "drop_off_picture_mandatory": True
            }
        },
        "client_code": "swiggy001",
        "pickup_details": {
            "longitude": 77.609680,
            "address": pickup_address,
            "latitude": 12.934247,
            "city": "Bangalore",
            "contact_number": "7503139350",
            "name": "Sandwedges"
        }
    }
    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    print(response.status_code, "========")
    return response.json()



if __name__ == "__main__":
    print(os.getenv('SHADOWFAX_API_KEY'), "========")
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        print(e)
