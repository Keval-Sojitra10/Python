import random
lis = [random.randint(1,30) for _ in range(20)]
n = int(input("Enter a number: "))
occ = lis.count(n)
c =0
for x in lis:
    if x==n:
        c=c+1
if c>0:
    print("Number of occurrences of ", n, "is", c)
        
