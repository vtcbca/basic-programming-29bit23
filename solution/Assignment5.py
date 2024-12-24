def is_palindrome_3(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    if len(s) <= 1:  # Base case: empty or one character is always a palindrome
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_3(s[1:-1])

# Test
input_string = "A man a plan a canal Panama"
print(f"Is palindrome? {is_palindrome_3(input_string)}")
