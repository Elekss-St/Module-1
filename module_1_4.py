my_string = input("Введите любую строку: ")
if not my_string:
    my_string = "Это тестоваЯ стрОка!"
    print ("Вы ввели пустую строку, мы  предлагаем следующую: '", my_string, "'", sep = "")
print("Длина этой строки равна",len(my_string))
print ("Строка в верхнем регистре -", my_string.upper())
print ("Строка в нижнем регистре -", my_string.lower())
print ("Строка без пробелов -", my_string.replace(" ",""))
print ("Первый символ строки -", my_string[0])
print ("Последний символ строки - ", my_string[-1])