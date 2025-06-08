import boto3
import json

sns = boto3.client('sns')

SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:102227939116:portfolio-webiste-notifications'

def lambda_handler(event, context):
    record = event['Records'][0]

    if record['eventName'] == 'INSERT':
        new_image = record['dynamodb']['NewImage']

        # Convert DynamoDB JSON format to plain JSON
        inserted_data = {key: list(value.values())[0] for key, value in new_image.items()}
        name = inserted_data["name"]
        subject = inserted_data["subject"]
        message = inserted_data["message"]
        email = inserted_data["email"]
        message = f"{name} had posted a message regarding {subject}. Content : {message}. Contact:{email}"

        # Send SMS via SNS
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject='New DynamoDB Record'
        )

    return {'statusCode': 200, 'body': 'SNS message sent'}
