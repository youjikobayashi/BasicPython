

n = int(input("n="))
def judgement(n):
    if n < 2:
        return ("判定できません。")
    else:
        if n == 2:
            return True
        for a in range(2,n): 
            if n%a == 0:
                return False
            elif a == n - 1:
                return True

print(judgement(n))