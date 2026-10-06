name = input('Введите ФИО')

sost = name.split()
if len(sost)>=3:
    fam = sost[0].capitalize()
    nam = sost[1].capitalize()
    otch = sost[2].capitalize()
    
    
    print(f'{fam} {nam[0]}. {otch[0]}.')
else:
    print('введите ФИО через пробел!!!!!!!!!!!!!!')

