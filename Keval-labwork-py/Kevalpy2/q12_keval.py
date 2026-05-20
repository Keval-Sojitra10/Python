x= int(input("Enter centre's x: "))
y= int(input("Ënter centre's y: "))
r= int(input("Ënter radius: "))
x1= int(input("Enter x1: "))
y1= int(input("Ënte y1: "))
dis= (((x1 - x)**2 + (y1 - y)**2))**0.5
if(dis > r):
    print("Point is outside the circle")
elif(dis<r):
    print("Point is inside the circle")
else:
    print("Point is on the circle")
