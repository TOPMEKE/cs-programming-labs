a = int(input())
b = int(input())
c = int(input())
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a+c <=b or b+c <= a:
    print('треугольник не существует')
elif a == b and b ==c :
    print('равносторонний')
elif a == b or a == c or b == c:
    print('равнобедренный')
else:
    print('разносторонний')
    
