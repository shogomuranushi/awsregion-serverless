import json

def create(event, context):
    body = u"create"

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

if __name__ == '__main__':
   result = readAll(None, None)
   print(result)
