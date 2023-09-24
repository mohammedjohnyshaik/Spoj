a = int(input("no of cases"))
results = []

def reverse_number(num):
    if num <= 9:
        return num
    else:
        conv_num = int(str(num)[::-1])
        return conv_num

for i in range(a):
    x, y = map(int, input().split())
    x = reverse_number(x)
    y = reverse_number(y)
    result = reverse_number(x + y)
    print(result)
    results.append(result)

for result in results:
    print(reverse_number(result))

'''Sample input: 
3
24 1
4358 754
305 794

Sample output:
34
1998
1'''