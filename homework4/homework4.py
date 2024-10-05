a =input ("Введите первое число: ")
b =input ("Введите второе число:")
def number(a, b):
    a = int (a)
    b = int (b)
    if a < b - 1:
        print (a+1)
        number (a+1, b)
    if b < a - 1:
        print(b + 1)
        number(b + 1, a)
    if a == b:
        print ('Числа равны')
try:
    a =float (a)
    b =float (b)
    print (number(a, b))
except ValueError:
    print("Невозможно произвести код: введите целое число.")
