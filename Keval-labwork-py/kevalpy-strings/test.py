str = ("PDEU College")
print(str[ :5])
print(str[5:])
print(str[3:])
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
