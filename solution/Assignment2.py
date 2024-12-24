def is_prime_3(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
test_numbers = [11, 14, 23, 35, 17]
for number in test_numbers:
    print(f"Is {number} prime? {is_prime_3(number)}")
