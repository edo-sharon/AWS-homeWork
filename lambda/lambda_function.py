import json
import boto3
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event

    num1 = body['num1']
    num2 = body['num2']
    total = num1 + num2

    message = f"The sum of {num1} and {num2} is {total}"

    sns.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message=message,
        Subject="Lambda Sum Result"
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'result': total})
    }
