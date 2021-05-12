from RandomNumberGenerator import RandomNumberGenerator


def instanceGenerator(Z, size):
    generator = RandomNumberGenerator(Z)
    d = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            if (i > j):
                d[i][j] = generator.nextInt(1, 50)
                d[j][i] = generator.nextInt(1, 50)

    return d