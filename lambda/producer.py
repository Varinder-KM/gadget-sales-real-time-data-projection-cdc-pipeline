import json
import random
import boto3
import time
from decimal import Decimal
from datetime import datetime

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('gadget-salse-data-tbl')
    products = {
        "Laptop": 800,
        "Smartphone": 600,
        "Tablet": 300,
        "Smartwatch": 200,
        "Headphones": 100,
        "Monitor": 250
        }
    timeout = 0

    while True and timeout<30:
        id = random.randint(1, 1000)
        product = random.choice(list(products.keys()))
        unite = random.randint(1, 100)
        unite_price = products[product]
        revenue = unite*unite_price
        profit = Decimal(revenue*0.3)
        create_at =  datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        recode = {
            "id": id,
            "product": product,
            "unite": unite,
            "unite_price": unite_price,
            "revenue": revenue,
            "profit": profit,
            "create_at": create_at
        }
        response = table.put_item(
            Item=recode
        )
        print(response)
        time.sleep(3)
        timeout+=3
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
