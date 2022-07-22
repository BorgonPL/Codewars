from math import sqrt, ceil
def nearest_sq(n):
    return pow(ceil(sqrt(n)),2) if ceil(sqrt(n))-n < round(sqrt(n))-n else  pow(round(sqrt(n)),2)