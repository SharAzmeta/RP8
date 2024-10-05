s =0
while True:
    print ("Введите число или остановите (stop или end)")
    num = input()
    if num == "stop" or num == "end":
        print (s)
        break
    else:
        try:
            num=float(num)
            s =s + num
        except ValueError:
            print("Невозможно произвести код: введите целое число.")
