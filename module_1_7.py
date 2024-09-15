# Определение массивов
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# подсчет среднего арифметического в массиве оценок c помощью for
# grade =  [ sum(count)/len(count) for count in grades]
# Создание словаря
# result = dict(zip(sorted(students),grade))
# Вывод результата
# print (result)
print (dict(zip(sorted(students),[ sum(count)/len(count) for count in grades])))