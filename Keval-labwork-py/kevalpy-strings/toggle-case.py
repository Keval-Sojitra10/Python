str= (input("Enter a string"))
toggle_case_result=" "
for char in str:
    if 'a'<=char<='z':
        toggle_case_result += chr(ord(char) -32)
    elif 'A'<=char<='Z':
        toggle_case_result += chr(ord(char) +32)
    else:
        toggle_case_result+= char
print(f"toggle string is {toggle_case_result}")
