import json

def lambda_handler(event, context):
    msg = "hello world with anuj and team!!!!!"
    return {"statusCode": 200, "body": json.dumps(msg)}
