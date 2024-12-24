def reverse_string_3(s):
    if len(s) == 0:  # Base case: empty string
        return s
    else:
        return reverse_string_3(s[1:]) + s[0]  # Recurse with the rest of the string

# Test
input_string = "Hello, World!"
print(f"Reversed string: {reverse_string_3(input_string)}")
