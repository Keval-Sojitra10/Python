num= int(input("Enter a number:"))
if(num<10):
    print("One digit")
elif(num<100):
    print("Two digits")
elif(num<1000):
    print("Three digits")
else:
    print("More than 3 digits")
