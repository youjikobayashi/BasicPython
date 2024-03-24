a = int(input())
b = int(input())
def euclid(a,b):
    
    if a>b:
        while b>0:
            if a%b == 0:
                return b
                break
            c = a%b
            a, b = b, c
    else:
        while a>0:
            if b%a ==0:
                return a
                break
            c = b%a
            a,b = c , a
        
def so(a,b):
    if euclid(a,b) == 1:
        return True
    else:
        return False

print (so(a,b))
