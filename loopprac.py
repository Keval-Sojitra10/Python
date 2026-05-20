sum=0
a= int(input("Enter no. "))
i=0
while i<=a:
    sum+=i
    i+=1
print("Sum is ",sum)

fact=1
n= int(input("Enter a number "))
for j in range(1,n+1):
    fact*=j
print("Factorial is ",fact)
