s = input("Enter string: ")

def count_vc(s):
    v=c=0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c
v,c = count_vc(s)
print("Vowels: ", v)
print("Consonants: ", c)