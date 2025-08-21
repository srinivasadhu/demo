import json

def lambda_handler(event, context):
    print("It's a sample hello app")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
