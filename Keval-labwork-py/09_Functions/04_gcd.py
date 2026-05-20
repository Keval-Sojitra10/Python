def gcd(n,d):
    if n%d==0:
        return d
    else:
        return gcd(d,n%d)
print(gcd(8,44678988))
