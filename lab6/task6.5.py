n = int(input())

if n < 1 or n > 10:
    print("Ошибка")
else:
    for i in range(n):
        row = []
        for j in range(n):
            distance = abs(i - j)
            row.append(distance)
        print(row)
