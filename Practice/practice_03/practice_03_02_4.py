# Задание 4: Расписание дня
"""
Создайте переменные:
- task1 = "встреча"
- time1 = 10
- task2 = "обед"
- time2 = 13
Сформатируйте строку:
"10:00 - встреча, 13:00 - обед."
"""
# Создаем переменные
task1 = "встреча"
time1 = 10
task2 = "обед"
time2 = 13

# Форматируем строку
formatted_string = f"{time1:02d}:00 - {task1}, {time2:02d}:00 - {task2}."

# Выводим результат
print(formatted_string)
