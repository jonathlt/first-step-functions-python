def handler(event, context):

    name = event.get('name',None)
    if name:
        greeting = "Hello " + name
    else:
        greeting = "Aye"

    return { 'message': greeting }
