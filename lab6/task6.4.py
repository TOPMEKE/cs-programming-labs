n = int(input())

if n < 0:
    print("Ошибка")
else:
    count = len(str(n))
    sum_digits = 0
    
    while n > 0:
        digit = n % 10
        sum_digits += digit
        n //= 10
    
    print(f"Цифр: {count}")
    print(f"Сумма цифр: {sum_digits}")
