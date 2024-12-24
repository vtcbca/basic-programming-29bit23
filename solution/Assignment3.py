def fibonacci_3(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_3(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Test
n_terms = 10
print(f"Fibonacci sequence with {n_terms} terms (recursive): {fibonacci_3(n_terms)}")
