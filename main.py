import numpy as np
import scipy.stats as st
import stats.chengSpring as chengSpring
import stats.moran as moran
import stats.sherman as sherman
from monteCarlo import monteCarlo

#количество наблюдений в выборке
n = 100
#количество выборок
N = 1000

def generateFunc(case = 0):
    if case is 0:
        return lambda:np.random.uniform(0, 1, n);
    if case is 1:
        return lambda:st.beta.rvs(1.22, 0.9, size=n)
    if case is 2:
        return lambda:st.beta.rvs(1.0, 0.75, size=n)
    if case is 3:
        return lambda:st.beta.rvs(0.8, 1.08, size=n)
    if case is 4:
        return lambda:st.gennorm.rvs(beta=8, loc=0.5, scale=0.5, size=n)
    if case is 5:
        return lambda:st.gennorm.rvs(beta=8, loc=0.45, scale=0.5, size=n)
    return lambda:st.gennorm.rvs(beta = 8, loc = 0.5, scale = 0.4, size=n)

def statFunc(case = 'chengSpring'):
    if case is 'chengSpring':
        return chengSpring.stat
    if case is 'moran' or case is 'moran1':
        return moran.stat1
    if case is 'moran2':
        return moran.stat2
    if case is 'sherman':
        return sherman.stat
    if case is 'shermanNormalized':
        return sherman.statNormalized
    return sherman.statModified


statNames = [
    'chengSpring',
    'moran',
    'moran2',
    'sherman',
    'shermanNormalized',
    'shermanModified',
]

hypotises = range(0, 7)

for statName in statNames:
    for hypotise in hypotises:
        print(statName, 'for hypotise', hypotise)
        statF = statFunc(statName)
        generateF = generateFunc(hypotise)
        statSample = monteCarlo(N, n, statF, generateF, statName, hypotise is 0)
        f = open(f'./output/H{hypotise}_{statName}_n={n}_N={N}.dat', 'w')
        f.write(f'H{hypotise}_{statName}_{n}\n')
        f.write(f'0 {n}\n')
        for item in statSample:
            f.write(f'{item}\n')
        f.close()
