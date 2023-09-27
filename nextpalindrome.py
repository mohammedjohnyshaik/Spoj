def next_palindrome(number):
    while True:
        number += 1
        if str(number) == str(number)[::-1]:
            return number
t = int(input())
numbers = [int(input()) for _ in range(t)]
for K in numbers:
    result = next_palindrome(K)
    print(result)
