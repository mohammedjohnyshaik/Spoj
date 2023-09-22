numbers = []
while True:
    num = input("")
    if num.isdigit and len(num) <= 2:
        if int(num) == 42:
            break
        numbers.append(int(num))
    else:
        break
for num in numbers:
    print(num)