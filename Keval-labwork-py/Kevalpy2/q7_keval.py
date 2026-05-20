yr= int(input("Enter any year more than 1000: "))
if(yr%4==0 and yr!=100):
    print("Leap year")
else:
    print("Not a leap year")
