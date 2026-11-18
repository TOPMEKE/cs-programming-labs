a = int(input())
b = int(input())

# Check for negative numbers or both being zero
if (a < 0 or b < 0) or (a == 0 and b == 0):
    print("Ошибка")
else:
    # Euclid's algorithm iterative approach
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    
    print(f"НОД: {a}")




#a = int(input('введи а'))
#b = int(input('введи b'))
#maxa = max(a,b)
#chislo =[]
#if a==0 and b == 0 or ((a < 0) or (b < 0)):
#    print('ошибочка')
#    
#else:
#    for i in range(1, maxa+1):
#        if ((a % i) == 0) and ((b % i) == 0):
#            chislo.append(i)
#        print(max(chislo))