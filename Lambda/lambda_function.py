import json

def lambda_handler(event, context):
    msg = "hello world with anuj and team, changing lambda now after creating the s3 website hosting, xD!!!!!"
    return {"statusCode": 200, "body": json.dumps(msg)}
