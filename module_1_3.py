name  = input("Введите ваше имя: ")
age  = input("Введите ваш возраст (целое число): ")
try:
    int(age)
except:
    print('Это не похоже на целое число, примем Ваш возраст за 54'); age=54
print ("Name:", name)
print ("Age:", age)
age = int(age) + 1
print ("New Age:", age)
is_student = True
print ("Is Student:", is_student)