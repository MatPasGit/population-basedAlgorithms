import random, math

def swaping(list):
    a = random.randint(0, len(list)-1)
    b= 0
    while a == b:
        b = random.randint(0, len(list)-1)

    buf = list[a]
    list[a] = list[b]
    list[b] = buf
    return list

def backwards(list):

    a = random.randint(0, len(list)-1)
    b = 0
    while math.fabs(a-b) <= 1:
        b = random.randint(0, len(list)-1)

    if (a<b):
        c= []
        for i in range(a ,b):
            c.append(list[i])
        c.reverse()
        for i in range(a ,b):
            list[i] = c[i-a]
    else:
        c = []
        for i in range(b, a):
            c.append(list[i])
        c.reverse()
        for i in range(b, a):
            list[i] = c[i-a]

    return list
