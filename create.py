#from prettyprint import pp
import pprint
pp = pprint.PrettyPrinter(indent=4)
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table    = dynamodb.Table('regions')

def create(event, context):
    try:
        if len(event['body']) == 0:
            return 'There is no data'

#	pp.pprint(event)
        body = event['body']

	json_data = json.loads(body.encode('utf-8'))
	region = json_data['region']
	jpname = json_data['jpname']

	table.put_item(
	    Item={
	        "region": region ,
	        "jpname": jpname
	   }
	)

        response = {
            "statusCode": 200,
            "body": body
        }

        return response

    except Exception as e:
        return e

if __name__ == '__main__':
    result = create(None, None)
    print(result)
