import random


def swaping(list):
    a = random.randint(0, len(list))
    b= 0
    while a !=b:
        b = random.randint(0, len(list))

    buf = list[a]
    list[a] = list[b]
    list[b] = buf
    return list

def backwards(list):
    a = random.randint(0, len(list))
    b = 0
    while a !=b:
        b = random.randint(0, len(list))

    if (a<b):
        c= []
        for i in range(a ,b):
            c = list[i]
        c.reverse()
        for i in range(a ,b):
            list[i] = c[i]
    else:
        c = []
        for i in range(b, a):
            c = list[i]
        c.reverse()
        for i in range(b, a):
            list[i] = c[i]

    return list