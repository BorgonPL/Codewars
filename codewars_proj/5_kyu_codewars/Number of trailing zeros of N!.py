def zeros(n):
    return sum(n//(5**a) for a in range(1,1000) if (n/(5**a) >= 1))