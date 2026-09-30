#расчет стоимости поездки
print('введите расстояние поездки')
Len = int(input())
print('введите расход топлива на 100 км')
Fuel= int(input())
print('введите стоимость литра топлива')
Price=float(input())
print(f'топливо:{(Fuel/100)*Len}L \nстоимость:{((Fuel/100)*Len)*Price} rub')

#L стоимость:{((Fuel/100)*len)*Price} rub'
