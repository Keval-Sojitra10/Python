def prime_fact(n, i=2):
    if n==1:
        return 1
    if n%i ==0:
          print(i, end= " ")
          prime_fact(n//i, i)
    else:
        prime_fact(n, i+1)

n = 24
print(prime_fact(n,i=2))
