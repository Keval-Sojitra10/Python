n  = int(input("Enter a number: "))
def prime_factors(n):
    factors = []
    i=2
    while i<=n:
        if n%i == 0:
            factors.append(i)
            n//=i
        else:
            i+=1
    return factors
    
print("Prime factors: ", prime_factors(n))