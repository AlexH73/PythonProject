# Задание 1: Представление профиля пользователя
"""
Создайте переменные:
- username = "Алиса"
- points = 145
Используя старый стиль форматирования, создайте строку:
"Пользователь Алиса заработал 145 баллов."
"""
# Создаем переменные
username = "Алиса"
points = 145

# Используем старый стиль форматирования
formatted_string = "Пользователь %s заработал %d баллов." % (username, points)

# Выводим результат
print(formatted_string)
