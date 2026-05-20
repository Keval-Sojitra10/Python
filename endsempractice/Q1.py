n = int(input("Enter number of integers you want to input: "))
lst = []
for i in range(0,n):
    element= int(input("Enter an integer:"))
    lst.append(element)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def remove_primes(lst):
    return list(filter(lambda x: not is_prime(x), lst))
result = remove_primes(lst)
print("List after removing primes:", result)
