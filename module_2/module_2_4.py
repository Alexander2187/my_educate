numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
num = 0

for i in range(len(numbers)):
    num = numbers[i]
    if (num == 2):
        primes.append(num)
        continue
    elif (num > 2):

        for k in range(2, num):
            is_prime = ((num % k) == 0)
            if is_prime:
                not_primes.append(num)
                break
            elif (k == (num - 1)):
                primes.append(num)
                break

print(primes)
print(not_primes)
