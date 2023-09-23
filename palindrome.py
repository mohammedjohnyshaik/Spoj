def is_palindrome(string):
    return string == string[::-1]

def find_smallest_palindrome_larger_than_k(k):
    while True:
        k += 1
        if is_palindrome(str(k)):
            return k
t = int(input())
for _ in range(t):
    k = int(input())
    result = find_smallest_palindrome_larger_than_k(k)
    print(result)
