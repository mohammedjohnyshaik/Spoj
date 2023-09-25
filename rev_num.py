def rev_num(num):
    sum = 0
    sign = 1
    if num < 0:
        sign = -1
        num = num * -1
    while num > 0:
        rem = num % 10
        sum = sum * 10 + rem
        num = num // 10
    return sum * sign
num = int(input("num: "))
reversed_num = rev_num(num)
print("Reversed num:", reversed_num)
