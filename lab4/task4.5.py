year = int(input())

if year < 1 or year > 9999:
    print("ошибка")
elif year % 400 == 0 or (year % 4 ==0 and year % 100 !=0):
    print('високосный')
else:
    print('невысокосный')
