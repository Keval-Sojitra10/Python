lst = list(map(int, input("Enter numbers:").split()))
def palindrome(lst):
    res = []
    for item in lst:
        if str(item) == str(item)[::-1]:
            res.append(item)
    return res
print("Palindrome numbers:", palindrome(lst))