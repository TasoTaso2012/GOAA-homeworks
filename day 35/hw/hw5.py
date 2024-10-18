def is_palindrome(s):
    return s == s[::-1]

result = is_palindrome("wow")
print(result)  

result = is_palindrome("hello")
print(result) 