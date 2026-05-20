s = input()
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count+=1
    return count

print(f"The number of vowels in '{s}' is: {count_vowels(s)}")