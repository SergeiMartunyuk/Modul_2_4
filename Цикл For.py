numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
index = 0
for i in range(len(numbers)):
    index = numbers[i]
    if index <= 1:
        continue
    is_prime = True
    for j in range(2, int(index ** 0.5) + 1):
        if index % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(index)
    else:
        not_primes.append(index)
print(primes)
print(not_primes)
