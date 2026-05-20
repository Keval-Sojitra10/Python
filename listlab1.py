import random
rando = []
for i in range(50):
    rando.append(random.randint(1,30))
print(rando)
rando = list(set(rando))
print(rando)