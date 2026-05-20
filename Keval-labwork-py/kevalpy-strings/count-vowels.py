str= str(input("Enter a string: "))
vowels= "aeiouAEIOU"
count=0
for char in str:
    if char in vowels:
        count+=1
print(f"Number of vowels in string: {count}")

    
