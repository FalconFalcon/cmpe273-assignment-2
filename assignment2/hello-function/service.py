# -*- coding: utf-8 -*-

print "Loading function..."

import boto3


def lambda_handler(event, context):
    print("Hello World")
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    menuDB = dynamodb.Table('PizzaMenu')

    httpMethod = event.get('httpMethod')
    data = event.get('data')

    if httpMethod == "POST":
        menuDB.put_item(
            Item={
                "menu_id": data["menu_id"],
                "store_name": data["store_name"],
                "selection": data["selection"],
                "size": data["size"],
                "price": data["price"],
                "store_hours": data["store_hours"]
            }
        )

        return {
            "status": 200
        }