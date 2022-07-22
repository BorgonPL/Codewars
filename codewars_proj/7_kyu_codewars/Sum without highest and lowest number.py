def sum_array(arr):
    if arr==[] : arr.sort()
    return sum(arr[x] for x in range(1, len(arr)-1))