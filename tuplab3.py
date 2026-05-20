lst = [(), ("A",1), (), ("B",2), ("C",3), ()]
new_list = []
for i in lst:
    if i != ():
        new_list.append(i)

print("List after removing empty tuples:", new_list)
