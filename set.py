collection = {1,2,3,3,3,"example","example",67}#ignores duplicates
print(len(collection))
print(collection)
empty= set()#syntax for empty set
print(type(empty))
collection.add(4)
collection.remove(1)
print(collection)
set1= {4,5,6}
set2= {6,8,9}
print(set1.union(set2))
print(set1.intersection(set2))