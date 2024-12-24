def pattern_3(n, i=1):
    if i > n:
        return
    print("* " * i)
    pattern_3(n, i + 1)

# Test
n = 4
pattern_3(n)
