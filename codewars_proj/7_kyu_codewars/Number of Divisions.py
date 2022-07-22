def divisions(n, divisor):
    return 1 + divisions(n/divisor, divisor) if n >= divisor else 0