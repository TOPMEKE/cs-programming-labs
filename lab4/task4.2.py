price = float(input())
age = int(input())

if price <= 0 or age < 0 or age > 120:
    print('ошибка')
elif age <= 5:
    print(f'стоимость: {price*0} руб')
elif age <= 17:
    print(f'стоимость:{price*0.5} руб')
elif age <= 59:
    print(f'стоимость:{price * 1} руб')
else:
    print(f"стоимость:{price*0.7} руб")