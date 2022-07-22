def gimme(input_array):
    for x in range(3):
        if input_array[x] != max(input_array) and input_array[x] != min(input_array) :
            return x 

print(gimme([1,3,2]))