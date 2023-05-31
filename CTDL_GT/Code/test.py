def check(x):
    if (x - int(x)) ==0:
        return int(x)
    else:
        return x

n=int(input("nhap so"))
def isPowerOfFour(n):
    while n>=1:
        if isinstance(n,int) == False:
            return 'false'
            break
        else:
            n = n/4
            n=check(n)
            continue
    n=n*4
    if n==1:
        return 'true'
    else:
        return 'false'
print(isPowerOfFour(n))
