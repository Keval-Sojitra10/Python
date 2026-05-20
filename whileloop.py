#1
# i=100
# #num= int(input("enter a number:"))
# while i>=1:
#     print(i)
#     i-=1
# #2
# j=1
# while i<=100:
#     print(i)
#     i+=1
#3
# k=5
# n=1
# while n<=10:
#     print(n*k)
#     n+=1
# #4
# m=1
# while m<=10:
#     print(m**2)
#     m+=1
#5
p= int(input("Enter number to be searched:"))
tuple=(1,4,9,16,25,36,49,64,81,100)
i=0
found= False
while i<=9:
    if p== tuple[i]:
        print("Found the searched number, ",tuple[i])
        found= True
        break
    i+=1
if not found:   
    print("Number not found in the list")