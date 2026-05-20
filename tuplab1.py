names = [("jay","veer"), "shreya", "freya", ("aman","moksh"), "priya"]
boys=0
girls=0
for i in names:
    if isinstance(i,tuple):
        boys+= len(i)
    else:
        girls+=1
print(f"Number of girls are {girls}")
print(f"Number of boys are {boys}")