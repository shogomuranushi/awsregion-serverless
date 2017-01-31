import json

def readOne(event, context):
    body = u"readOne"

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

if __name__ == '__main__':
   result = readAll(None, None)
   print(result)
