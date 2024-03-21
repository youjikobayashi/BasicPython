a = int(input("a ="))
b = int(input("b ="))

if a>b:
    while b>0:
        if a%b == 0:
            print(b)
            break
        c = a%b
        a, b = b, c
else:
    while a>0:
        if b%a ==0:
            print(a)
            break
        c = b%a
        a,b = c , b
