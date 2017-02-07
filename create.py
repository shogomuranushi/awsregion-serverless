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

#####
	pp.pprint(body.encode('utf-8'))
	print(isinstance(body,unicode))
	print(isinstance(body,str))

#	json_data = json.dumps(body, ensure_ascii=False)
#	json_data = json.loads(body.encode('utf-8').replace("'",""))
	json_data = json.loads(body.encode('utf-8'))

	pp.pprint(json_data)
	region = json_data['region']
	jpname = json_data['jpname']

	pp.pprint(region)
	pp.pprint(jpname)

#####
	table.put_item(
	    Item={
	        "id": region ,
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
