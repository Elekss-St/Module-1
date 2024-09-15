count_DZ_end = input("Введите количество домашних заданий (числом) - ")
try:
    float(count_DZ_end)
except:
    print('Это не похоже на число , примем количество заданий за 12'); count_DZ_end=12
count_use_clock = input("Введите количество затраченных часов (числом) - ")
try:
    float(count_use_clock)
except:
    print('Это не похоже на число , примем количество часов за 1.5'); count_use_clock=1.5
name_cource = input("Введите название курса - ")
time_one_lesson = float(count_use_clock)/float(count_DZ_end)
print("Курс: ",name_cource,", всего задач:",count_DZ_end,", затрачено часов: ",count_use_clock,", среднее время выполнения ", time_one_lesson," часа.", sep = "")