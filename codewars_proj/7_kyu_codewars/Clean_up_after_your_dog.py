def crap(garden, bags, cap):
    r=0
    for e in garden:
        if e.count("D")>0:
            return "Dog!!"
        r+=e.count("@")
    if r>(bags*cap):
        return "Cr@p"
    else:
        return "Clean"