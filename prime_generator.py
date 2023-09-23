def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

t = int(input("Enter the number of test cases: "))

for _ in range(t):
    m, n = map(int, input().split())
    for num in range(m, n + 1):
        if is_prime(num):
            print(num)
    print()
