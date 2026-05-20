str= (input("Enter a string"))
l = len(str)
if(l%2==0):
    first= str[0]
    print(f"First letter of string is {first}")
    last= str[l-1]
    print(f"Last letter of string: {last}")
    print("Middle character NA")
if(l%2!=0):
    one= str[0]
    print(f"First letter of string is {one}")
    latest= str[l-1]
    print(f"Last letter of string: {latest}")
    mid= str[(l-1)//2]
    print(f"Middle character: {mid}")
    
