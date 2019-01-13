import numpy as np

def stat(sample):
    variation_series = np.sort(sample)
    n = len(variation_series)
    one_by_n = 1 / (n + 1)

    w = 0
    i = 0

    while i < len(sample):
        u_cur = variation_series[i]
        u_prev = 0
        if i != 0:
            u_prev = variation_series[i - 1]

        w += 1 / 2 * np.abs(u_cur - u_prev - one_by_n)
        i = i + 1

    return w

def get_m(n):
    return (n/(n + 1)) ** (n + 1)

def get_d(n):
    numerator = (2 * n) ** (n + 2) + n * ((n - 1) ** (n + 2))
    denominator = (n + 2) * ((n + 1) ** (n + 2))
    subtrahend = (n / (n + 1)) ** (n + 2)
    return numerator/denominator - subtrahend

def statNormalized(sample):
    n = len(sample)
    m = get_m(n)
    d = get_d(n)

    return (stat(sample) - m) / np.sqrt(d)

def statModified(sample):
    n = len(sample)
    u = (stat(sample) - (0.3679 * (1 - (1 / (2 * n))))) / ((0.2431 / np.sqrt(n)) * (1 - (0.605 / n)))
    return u - (0.0955/np.sqrt(n)) * (u ** 2 - 1)