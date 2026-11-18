n = int(input())

if n < 2:
    print("Ошибка")
else:
    i = 2
    result = []
    
    while n > 1:
        if n % i == 0:
            result.append(str(i))
            n //= i
        else:
            i += 1
    
    print(result)