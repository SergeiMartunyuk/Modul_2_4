numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_primes = True
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_primes = False
            break
    if is_primes:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)