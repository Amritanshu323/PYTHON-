def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def first_n_primes_with_min_digits(n, min_digits):
    primes = []
    num = 100 if min_digits < 3 else 10 ** (min_digits - 1)
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes

n = 20
min_digits = 3
prime_numbers = first_n_primes_with_min_digits(n, min_digits)

print("First 20 prime numbers with at least 3 digits:")
for prime in prime_numbers:
    print(prime)
