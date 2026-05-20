def count_alpha_digits(s):
    d = {}
    alp = 0
    dig = 0
    for i in s:
        if i.isalpha():
            alp += 1
        elif i.isdigit():
             dig += 1
    d["alphabets"] = alp
    d["digits"] = dig
    return d
st = input("Enter a string: ")
ans = count_alpha_digits(st)
print(ans)        
    
