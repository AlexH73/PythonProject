# 5. Перевёрнутое предложение:
"""
Напишите метод reverse_sentence, который принимает предложение в качестве аргумента.
Метод должен вернуть предложение с перевёрнутым порядком слов.
Пример: Для "Я люблю Python" метод должен вернуть "Python люблю Я".
"""
# Назначаем функцию.
def reverse_sentence(proposal):
    # Разделяем фразу на слова.
    word1 = proposal.split()[0]
    word2 = proposal.split()[1]
    word3 = proposal.split()[2]
    # Формируем возврат
    return word3 + ' ' + word2 + ' ' + word1
# Проверяем функцию.
print(reverse_sentence("Я люблю Python"))