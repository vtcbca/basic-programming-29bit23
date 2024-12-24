def print_row(i, n):
    if i > n:
        return
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print the increasing part
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    
    # Print the decreasing part (excluding the last element)
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end=" ")
    
    print()  # Newline
    
    # Recursively call for the next row
    print_row(i + 1, n)

def alphabet_pattern_3(n):
    print_row(1, n)

# Test
n = 3
alphabet_pattern_3(n)
