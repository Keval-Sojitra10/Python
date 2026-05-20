a= int(input("Enter A: "))
b= int(input("Ënter B: "))
c= int(input("Ënter C: "))
if(a>=b and b>=c):
    print("Largest is ",a)
    print("Smallest is ",c)
elif(b>=c and c>=a):
    print("Largest is ",b)
    print("Smallest is ",a)
elif(c>=a and a>=b):
    print("Largest is ",c)
    print("Smallest is ",b)
elif(a>=c and c>=b):
    print("Largest is ",a)
    print("Smallest is ",b)
elif(b>=a and a>=c):
    print("Largest is ",b)
    print("Smallest is ",c)
elif(c>=b and b>=a):
    print("Largest is ",c)
    print("Smallest is ",a)
else:
    print("All numbers are equal")
