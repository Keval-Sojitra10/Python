str=input ("Enter the string")
c=0;d=0

for ch in str:
    if ch.isalpha():
        c+=1
    elif ch.isdigit():
        d+=1
        
print("Alphabets are :",c)
print("Alphabets are :",d)
