# s =  input("Enter sentence:")
# def reverse(s):
#     #words = s.split()

#     for w in s:
#         rev = w[::-1]
#     return " ".join(rev)
# print(reverse(s))


def reverse_words(s):
    words = s.split()
    rev = [w[::-1] for w in words]
    return " ".join(rev)

s = input("Enter sentence: ")
print(reverse_words(s))