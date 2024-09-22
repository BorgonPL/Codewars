def chose_rating(list):
    rating = [5.0,4.5,4.0,3.5,3.0,2.0]
    for i in rating:
        if i <= ((sum(list)/len(list))+0.25 if len(list)>0 else 0):
            return i
    return "no ratings"


list=[3,2,3,2.5]
print((sum(list)/len(list)))
print(chose_rating(list))

