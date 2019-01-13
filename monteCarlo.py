def monteCarlo(N, n, statFunc, generateFunc, generateName, isH0):
    statistica = []
    for i in range(N):
        x = list(generateFunc())
        statistica.append(statFunc(x))
        if (i%100 == 0):
            print(f'Done {i/N * 100}% MonteCarlo {generateName} {isH0}')
    return statistica
