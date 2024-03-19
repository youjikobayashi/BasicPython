

# TODO
n = 61
for a in range(2,n):
    if n == 1:
        print ("素数ではない。")
        break
    if n == 2:
        print ("素数である。")
        break
        
    if n%a == 0:
        print ("素数ではない。")
        break
    else:
        if a == n - 1:
            print ("素数である。")

n = 10
for a in range(2,n):
    if n == 1:
        print ("素数ではない。")
        break
    if n == 2:
        print ("素数である。")
        break
    if n%a == 0:
        print ("素数ではない。")
        break
    else:
        if a == n - 1:
            print ("素数ではない")
