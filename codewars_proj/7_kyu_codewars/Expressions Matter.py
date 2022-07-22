def expression_matter(a, b, c):
    if a <= 1:
        b+=a
        if c <= 1:
            b+=c
            return b
        return b*c
    if c <= 1:
        b+=c
        return a*b
    if b<=1:
        b+= min(a,c)
        return max(a,c) * b
    return a*b*c