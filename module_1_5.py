immutable_var = (1,2,3,True,"строка", [1,2,3])
print ( type(immutable_var),"Это кортеж :",  immutable_var )
# Изменения элементов кортежа не поддерживаются, но можно поменять содержимое элемента список внутри кортежа
immutable_var[5][2] = 'три'
print ( type(immutable_var),"Это измененный список в кортеже:",  immutable_var )
mutable_list =[ 1,2,3,True,"Строка", [1,2,3]]
print (type(mutable_list), "Это изменяемый список,\n можно изменить любой элемент в нем:", mutable_list)
mutable_list[4] = False
mutable_list[3] = 5
mutable_list[2] = "str"
mutable_list[5][2] = 1
mutable_list[5][0] = 3
print (type(mutable_list), "Это изменённый список ", mutable_list)