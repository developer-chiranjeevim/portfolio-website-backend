import json
import boto3

dynamo_db = boto3.resource('dynamodb')
table = dynamo_db.Table('portfolio-website-leads')

def add_record(data):
    try:  
        table.put_item(Item=data)
        return True

    except Exception as e:
        return e



if __name__ == "__main__":
    #driver code
    response = add_record({
            "email" : "developer.chiranjeevim@gmail.com",
            "name" : "chiranjeevi",
            "subject" : "test subject",
            "message" : "test message"
    })
    print(response)