def gauss(n, k):
    calculated = 1
    for i in range(1, k+1):
        calculated *= (n - i + 1) / i
    return calculated
