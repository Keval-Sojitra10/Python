def count_upper_lower(str):
    lower = 0
    upper = 0
    for ch in str:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
    print("Lowercase:", lower)
    print("Uppercase:", upper)
s = input("Enter string:")
count_upper_lower(s)
        
        
        
