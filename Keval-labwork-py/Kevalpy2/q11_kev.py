x1= int(input("Enter x1: "))
y1= int(input("Ënter y1: "))
x2= int(input("Ënter x2: "))
y2= int(input("Enter y2: "))
x3= int(input("Ënter x3: "))
y3= int(input("Ënter y3: "))
m1= (y2 - y1)/(x2 - x1)
m2= (y3 - y2)/(x3 - x2)
if(m1==m2):
    print("Points are collinear")
    
else:
    print("Points are not collinear")

