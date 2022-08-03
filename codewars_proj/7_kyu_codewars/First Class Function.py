def factory(x):
    def func(my_arr):
        return [x*my_arr[y] for y in range(len(my_arr))]
    return func