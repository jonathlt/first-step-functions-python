import json

def handler(event, context):

    cause = json.loads(event['Cause'])
    received_error = cause['errorMessage']
    if received_error == "WrongName":
        errorMessage = "I dont know how to greet this name"
    elif received_error == "NoName":
        errorMessage = "Please give me a name to greet"
    else:
        errorMessage = "Unknown error"
    
    return { 'message': errorMessage }