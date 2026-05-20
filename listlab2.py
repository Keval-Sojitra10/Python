import random
lst=[]
neg = []
posi = []
for i in range(50):
    lst.append(random.randint(-50,50))
print(lst)
for i in lst:
    if lst[i] <0:
        neg.append(lst[i])
    else:
        posi.append(lst[i])
print(neg)
print(posi)
