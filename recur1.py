def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
show(8)

def factorial(a):
    fact=1
    if(a==1 or a==0):
        return 1
    fact= factorial(a-1) *a
    return fact
print(factorial(4))