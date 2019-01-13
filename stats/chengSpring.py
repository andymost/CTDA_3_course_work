def stat(x):
    x = sorted(x)
    n = len(x)
    mean = sum(x) / n
    numerator = ((x[n - 1] - x[0]) * ((n + 1) / (n - 1))) ** 2
    denominator = sum([(x[i] - mean) ** 2 for i in range(len(x) - 1)])
    return numerator / denominator
