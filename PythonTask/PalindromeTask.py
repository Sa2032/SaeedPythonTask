def is_palindrome(s):
    s = s.replace(" ", "").lower()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    is_palind = s == s[::-1]
    return (is_palind, char_count)

print(is_palindrome("momnmom"))  
print(is_palindrome("I Know"))  
