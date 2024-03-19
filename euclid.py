a = 10
b = 20

# TODO
if a>b:
    for i in range(b):
        c = a % b
        if c == 0:
            print(b)
            break
        if b % c == 0:
            print(c)
            break
        a = b % c
        if a == 0:
            print(b/c)
            break
        if c % a ==0:
            print(a)
            break
else:

    for i in range(a):
        c = b % a
        if c == 0:
            print(a)
            break
        if a % c == 0:
            print(c)
            break
        b = a % c
        if b == 0:
            print(a/c)
            break
        if c % b == 0:
            print(b)
            break
a = 14
b = 91
if a>b:
    for i in range(b):
        c = a % b
        if c == 0:
            print(b)
            break
        if b % c == 0:
            print(c)
            break
        a = b % c
        if a == 0:
            print(b/c)
            break
        if c % a ==0:
            print(a)
            break
else:
    for i in range(a):
        c = b % a
        if c == 0:
            print(a)
            break
        if a % c == 0:
            print(c)
            break
        b = a % c
        if b == 0:
            print(a/c)
            break
        if c % b == 0:
            print(b)
            break
a = 91
b = 14
if a>b:
    for i in range(b):
        c = a % b
        if c == 0:
            print(b)
            break
        if b % c == 0:
            print(c)
            break
        a = b % c
        if a == 0:
            print(b/c)
            break
        if c % a ==0:
            print(a)
            break
else:
    for i in range(a):
        c = b % a
        if c == 0:
            print(a)
            break
        if a % c == 0:
            print(c)
            break
        b = a % c
        if b == 0:
            print(a/c)
            break
        if c % b == 0:
            print(b)
            break
            
