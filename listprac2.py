list= [2,'xyz',5,'zyx',2]
copy = list.copy()
copy.reverse()
if(copy == list):
    print("List is a palindrome")
else:
    print("List is not a palindrome")