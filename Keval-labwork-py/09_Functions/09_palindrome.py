def palindrome(str):
    if str.lower() == str[::-1].lower():
        print("PALINDROME")
    else:
        print("NOT PALINDROME")
palindrome("LAsSI")
palindrome("abba")
palindrome("SARas")
        
