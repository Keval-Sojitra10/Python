def convert(s):
    #s = input("Enter a sentence:")
    new = set(list(s))
    sorted_list = sorted(new)
    joined = "".join(sorted_list)
    print(joined)
str1 = "ABC DEF ABC"
convert(str1)
    
