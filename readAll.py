import json

def readAll(event, context):
    body = u"list"

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

if __name__ == '__main__':
   result = readAll(None, None)
   print(result)
