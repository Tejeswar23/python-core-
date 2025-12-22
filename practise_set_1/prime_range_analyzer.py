A = int(input("Enter the starting number: "))
B = int(input("Enter the ending number: "))
prime_count = 0

for num in range(A, B + 1):
    if num > 1:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            prime_count += 1

print(prime_count)

