import json

def lambda_handler(event, context):
    msg = "hello world with anuj and team, this is the second lambda function in the CI/CD pipeline!!!!!"
    return {"statusCode": 200, "body": json.dumps(msg)}
