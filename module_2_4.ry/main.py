numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in numbers:
    print(i)
primes = []
not_primes = []
for i in numbers:
    count = 0
    is_prime = True
    if i == 1:
        continue
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count <= 2:
        primes.append(i)
    elif count > 2:
        not_primes.append(i)
print('Primes:', primes)
print('Not_primes:', not_primes)

