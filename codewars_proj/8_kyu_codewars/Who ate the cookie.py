def cookie(x):
    WhoAte="Who ate the last cookie? It was "
    if type(x)==str:
        return WhoAte + "Zach!"
    elif type(x)==int or type(x)==float:
        return WhoAte + "Monica!"
    else:
        return WhoAte + "the dog!"