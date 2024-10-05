while True:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    try:
        a =int (a)
        b =int (b)
        print ("Сумма: ", a+b)
        b = input ("Хотите продолжить? y/n")
        if b == "y":
            break

    except ValueError:
        print("Невозможно произвести код: введите целое число.")
