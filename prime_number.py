

# TODO
n = 61
if n == 1:
    print("素数ではない。")
if n == 2:
    print ("素数である。")
for a in range(2,n): 
    if n%a == 0:
        print ("素数ではない。")
        break
    else:
        if a == n - 1:
            print ("素数である。")

n = 10
if n == 1:
    print("素数ではない。")
if n == 2:
    print ("素数である。")
for a in range(2,n):
    if n%a == 0:
        print ("素数ではない。")
        break
    else:
        if a == n - 1:
            print ("素数ではない")
