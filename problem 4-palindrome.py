def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

test_string = "radar"
print(is_palindrome(test_string))  


