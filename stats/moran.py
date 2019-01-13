import numpy as np

def stat1(x):
    x.insert(0, 0)
    x.append(1)
    x = sorted(x)
    return sum([(x[i + 1] - x[i]) ** 2 for i in range(len(x) - 1)])


def stat2(x):
    x.insert(0, 0)
    x.append(1)
    x = sorted(x)
    n = len(x)
    return -sum([np.log((n + 1) * (x[i + 1] - x[i])) for i in range(len(x) - 1)])
