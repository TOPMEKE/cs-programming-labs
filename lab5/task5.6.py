n = int(input())

odd_count = 0

for r in range(n):
    current_val = 1
    
    # Печатаем первый элемент строки (всегда 1)
    print(current_val, end="") #edn="" делает перенос строки
    if current_val % 2 != 0:
        odd_count += 1
        
    # Вычисляем и печатаем последующие элементы текущей строки
    for k in range(r):
        current_val = current_val * (r - k) // (k + 1)
        print(f" {current_val}", end="")
        if current_val % 2 != 0:
            odd_count += 1
            
    # Переходим на новую строку (в конце строки пробела нет)
    print()

print(f"Нечетных элементов: {odd_count}")
