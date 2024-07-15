

def show( obj ):
    return[ item for item in dir( obj ) if not item.startswith('_') ]


