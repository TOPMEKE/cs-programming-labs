count = 0
total_price = 0

while True:
    user_input = input()
    if user_input == "stop":
        break
    
    price = int(user_input)
    count += 1
    total_price += price

if count == 0:
    print("Нет покупок")
else:
    average_price = total_price / count
    print(f"Покупок: {count}")
    print(f"Общая стоимость: {total_price} руб")
    print(f"Средняя стоимость: {average_price:.2f} руб")
