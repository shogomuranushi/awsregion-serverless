#from prettyprint import pp
import pprint
pp = pprint.PrettyPrinter(indent=4)
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('regions')

def readAll(event, context):
    try:
	data = table.scan()
	print(data)
	body = data

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
