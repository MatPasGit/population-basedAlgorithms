from RandomNumberGenerator import RandomNumberGenerator


def instanceGenerator(Z, size):
    generator = RandomNumberGenerator(Z)
    d = []
    d = [[0 for i in range(size)] for j in range(size)]
    w = []
    w = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if (i > j):
                d[i][j] = generator.nextInt(1, 50)
                d[j][i] = d[i][j]
                w[i][j] = generator.nextInt(1, 50)
                w[j][i] = w[i][j]

    return w, d