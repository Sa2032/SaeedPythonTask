import math
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

def is_prime(n):
    if n < 2:
        return []
    sqrt_n = int(math.sqrt(n))
    result = [(n % i == 0, i) for i in range(2, sqrt_n + 1)]
    
    return result
def main():
    results = []
    user_string = input("Enter a string: ")
    palindrome_result, char_count = is_palindrome(user_string)
    user_number = int(input("Enter a number: "))
    prime_result = is_prime(user_number)
    result_dict = {
        "input_string": user_string,
        "palindrome_result": palindrome_result,
        "char_count": char_count,
        "input_number": user_number,
        "prime_result": prime_result
    }
    
    results.append(result_dict)
    
    
    print(results)

if __name__ == "__main__":
    main()
