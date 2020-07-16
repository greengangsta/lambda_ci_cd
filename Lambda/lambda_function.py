import json

def lambda_handler(event, context):
    msg = "hello world"
    return {"statusCode": 200, "body": json.dumps(msg)}
