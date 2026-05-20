str= (input("Enter a string"))
upr_case_result=" "
for char in str:
    if 'a'<=char<='z':
        upr_case_result += chr(ord(char) -32)
    else:
        upr_case_result+= char
print(f"Uppercase string is {upr_case_result}")
