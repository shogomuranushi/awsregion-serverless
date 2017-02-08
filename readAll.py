#from prettyprint import pp
import pprint
pp = pprint.PrettyPrinter(indent=4)
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('regions')

def readAll(event, context):
    try:
        body = table.scan()
        print(body)
        print(body['Items'])
        
        data = ""
        for x in body['Items']:
            data += x['id'] + "\t" + x['jpname'] + "\n"

        response = {
            "statusCode": 200,
            "body": data
        }

        return response

    except Exception as e:
        return e

if __name__ == '__main__':
    result = readAll(None, None)
    print(result)
