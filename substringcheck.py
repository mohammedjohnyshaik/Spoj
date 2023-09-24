def is_substring(A, B):
    return B in A
n = int(input())
for _ in range(n):
    A, B = input().split()
    if is_substring(A, B):
        print("1")  
    else:
        print("0")  
