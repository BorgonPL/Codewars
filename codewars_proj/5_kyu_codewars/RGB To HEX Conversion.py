# def clamp(x): 
#   return max(0, min(x, 255))

# def rgb(*w):
#     return "".join(hex(clamp(x))[2:].zfill(2).upper() for x in w)

def rgb(*args):
    return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args))

print(rgb(400,-10,100))
