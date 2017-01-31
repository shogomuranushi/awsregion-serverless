import json

def delete(event, context):
    body = u"delete"

    response = {
        "statusCode": 200,
        "body": body
    }

    return response

if __name__ == '__main__':
   result = readAll(None, None)
   print(result)
