valid_names = ["Danilo", "Daniel", "Dani"]

class NameError(Exception): pass

def handler(event, context):

    name = event.get("name",None)

    if name:
        if name in valid_names:
            return event
        else:
            raise NameError("WrongName") 
    else:
        raise NameError("NoName")
