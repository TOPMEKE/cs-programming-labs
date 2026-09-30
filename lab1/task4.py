#время
print('введите секунды')
sec = (int(input()))
MM=sec//60
HH=MM//60
SS=sec%60
print(f'время:{HH}:{MM}:{SS}')