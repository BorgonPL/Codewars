def predict_age(*age):
    from math import floor 
    return floor(pow(sum(x**2 for x in age),1/2)/2)