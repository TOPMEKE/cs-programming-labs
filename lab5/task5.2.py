a = int(input())
b = int(input())

summ = 0
product = 1

for i in range(a, b + 1):
    summ += i
    product *= i

print("Сумма:", summ)
print("Произведение:", product)
