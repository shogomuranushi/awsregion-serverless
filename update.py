import json

def update(event, context):
    body = u"update"

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

if __name__ == '__main__':
   result = readAll(None, None)
   print(result)
