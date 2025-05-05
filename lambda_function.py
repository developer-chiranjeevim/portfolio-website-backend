import json
from main import add_record

def lambda_handler(event, context):
    data = json.loads(event['body'])

    response = add_record(data)
    if(response):
        return {
            "statusCode": 200,
            "body": json.dumps('record added successfully')
        }
    else:
        return {
            "statusCode" : 404,
            "body": json.dumps('cannot add record')
        }



