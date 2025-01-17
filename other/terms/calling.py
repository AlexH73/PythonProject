from terms import terms  # Если сохранили в файле terms.py

# Пример использования
for category, term_list in terms.items():
    print(f"**{category}**")
    for term in term_list:
        print(f"  Русский: {term.get('Русский', 'N/A')}, Немецкий: {term.get('Немецкий', 'N/A')}, Английский: {term.get('Английский', 'N/A')}")