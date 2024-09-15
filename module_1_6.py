# Создаем переменную и присваиваем ей значения словаря
my_dict = {"Алексей":2001,"Игорь":1987,"Борис":1999}
# Выводим значение переменной
print ( "Dict:", my_dict )
# Вывод одного значения по ключу
print ( "Existing value:", my_dict["Игорь"])
# "Вывод значения несуществующего ключа без ошибок
print ("Not existing value:",my_dict.get("Сергей"))
# Добавление одного значения способ 1
my_dict["Сергей"] = 1988
# Добавление одного значения способ 2
my_dict.update ({"Иван":1989})
# Удаление значения "Игорь"
a_tmp = my_dict.pop("Игорь")
# Печать удаленного значения
print ("Deleted value:",a_tmp)
# Печать всего словаря
print ("Modified dictionary:",my_dict )

# Создаем переменную my_set и присваиваем ей множество
my_set = {1,3,True,"ABC","abc",3,True,False,"True","False","False","3","abc",3,1,5,(3,1,5),(1,3,5)}
print ("\nSet:",my_set)
# Добавляем пару произвольных элементов
a_tmp = my_set.add(8)
a_tmp = my_set.add("aBc")
# Удаляем один элемент
a_tmp = my_set.discard(False)
# Выводим содержимое переменной my_set
print ("Modified set:",my_set)