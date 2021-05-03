n = 100
primes = []

for i in range(2, n):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
        
    if is_prime:
        primes.append(i)

print(primes)
