str= (input("Enter a string"))
lwr_case_result=" "
for char in str:
    if 'A'<=char<='Z':
        lwr_case_result += chr(ord(char) +32)
    else:
        lwr_case_result+= char
print(f"Uppercase string is {lwr_case_result}")
