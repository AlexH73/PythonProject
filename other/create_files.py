import os

# Назначаем функцию
def create_files(directory):
    # Логика создания файлов
    for i in range(1, 6):
        filename = f"practice_14_{i:02}.py"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w',  encoding='utf-8') as file:
            file.write("# Этот файл был создан автоматически\n")

# Вызов и вывод
directory = input("Введите путь к директории: ")
create_files(directory)
print("Файлы успешно созданы.")
