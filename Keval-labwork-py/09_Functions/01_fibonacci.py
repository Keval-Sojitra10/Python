def recfibo(n):
    if n==1:
        return 0
    elif(n==2):
        return 1
    else:
        return recfibo(n-1) + recfibo(n-2)
a = recfibo(4)
print(a)
