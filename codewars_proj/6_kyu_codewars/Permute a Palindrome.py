def permute_a_palindrome (input): 
    i=0
    for a in range(len(input)):
        if input.count(input[a])%2!=0:
            i+=1
    return True if i<=1 else False