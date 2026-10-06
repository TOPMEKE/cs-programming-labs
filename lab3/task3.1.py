code = input('Введите код документа в формате AAA-NNNN-NNNN')

cat = code[0:3]
god = code[4:8]
nomer = code[9:13]

obrnomer = code[::-1]
print(f'категория:{cat}')
print(f'год:{god}')
print(f'номер:{nomer}')
print(f'обратный номер:{obrnomer}')
