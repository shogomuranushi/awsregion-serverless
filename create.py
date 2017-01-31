import json
import boto3

def create(event, context):
    try:
        if len(event['body']) == 0:
            return 'There is no data'

        body = event['body']

        response = {
            "statusCode": 200,
            "body": body
        }

        return response

    except Exception as e:
        return e

if __name__ == '__main__':
   result = readAll(None, None)
   print(result)
