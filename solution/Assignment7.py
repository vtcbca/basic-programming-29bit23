def triangle_pattern_3(n):
    for i in range(1, n + 1):
        # Leading spaces
        print(" " * (n - i), end="")
        # Numbers in the current row
        print(*range(1, 2 * i))  # * is used to unpack the range

# Test
n = 3
triangle_pattern_3(n)
