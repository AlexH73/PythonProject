main_course_cash = 0
main_course_extra_cash = 0
salad_cash = 0
salad_extra_cash = 0
dessert_cash = 0
dessert_extra_cash = 0
drink_cash = 0
drink_extra_cash = 0

def main_course(dish):
    global main_course_cash, main_course_extra_cash
    if dish == "Пицца" or dish == "Пица" or dish == "1":
        main_course_cash = 5
        main_extra_change = input("Можете выбрать добавку:\n1. Сыр (+1.50€)\n2. Бекон (+2.00€)\n3. Острый соус (+1.00€)\n4. Отказаться \n").capitalize()
        main_course_extra_cash = extra_dish_pizza(main_extra_change)
        return f"Вы выбрали {dish}"
    elif dish == "Паста":
        main_course_cash = 6
        main_extra_change = input("Хотите добавить экстра: Пармезан (+1.20€), Грибы (+1.50€), Трюфельное масло (+3.00€)? или Отказаться \n").capitalize()
        main_course_extra_cash = extra_dish_pasta(main_extra_change)
        return f"Вы выбрали {dish}"
    elif dish == "Стейк":
        main_course_cash = 7
        main_extra_change = input("Хотите добавить экстра: Соус барбекю (+1.50€), Гарнир (картофель/овощи, +2.50€), Перечный соус (+2.00€)? или Отказаться \n").capitalize()
        main_course_extra_cash = extra_dish_steak(main_extra_change)
        return f"Вы выбрали {dish}"
    else:
        return "Вы отказались от заказа основного блюда!"

def extra_dish_pizza(extra):
    if extra == "Сыр":
        return 1.50
    elif extra == "Бекон":
        return 2.00
    elif extra == "Острый соус":
        return 1.00
    else:
        return 0

def extra_dish_pasta(extra):
    if extra == "Пармезан":
        return 1.20
    elif extra == "Грибы":
        return 1.50
    elif extra == "Трюфельное масло":
        return 3.00
    else:
        return 0

def extra_dish_steak(extra):
    if extra == "Соус барбекю":
        return 1.50
    elif extra == "Гарнир":
        return 2.50
    elif extra == "Перечный соус":
        return 2.00
    else:
        return 0

def salad_selection(salad):
    global salad_cash, salad_extra_cash
    if salad == "Цезарь":
        salad_cash = 8
        salad_extra_change = input("Хотите добавить экстра: Курица (+2.00€), Креветки (+4.00€), Дополнительный сыр (+1.00€)? или Отказаться \n").capitalize()
        salad_extra_cash = extra_dish_cesar(salad_extra_change)
        return f"Вы выбрали {salad}"
    elif salad == "Греческий":
        salad_cash = 9
        salad_extra_change = input("Хотите добавить экстра: Маслины (+0.50€), Дополнительный сыр Фета (+1.50€), Хрустящие гренки (+1.00€)? или Отказаться \n").capitalize()
        salad_extra_cash = extra_dish_greek(salad_extra_change)
        return f"Вы выбрали {salad}"
    elif salad == "Салат с тунцом":
        salad_cash = 10
        salad_extra_change = input("Хотите добавить экстра: Креветки (+4.00€), Авокадо (+2.50€), Яйцо (+0.50€)? или Отказаться \n").capitalize()
        salad_extra_cash = extra_dish_tuna(salad_extra_change)
        return f"Вы выбрали {salad}"
    else:
        return "Вы отказались от заказа салата!"

def extra_dish_cesar(extra):
    if extra == "Курица":
        return 2.00
    elif extra == "Креветки":
        return 4.00
    elif extra == "Дополнительный сыр":
        return 1.00
    else:
        return 0

def extra_dish_greek(extra):
    if extra == "Маслины":
        return 0.50
    elif extra == "Дополнительный сыр Фета":
        return 1.50
    elif extra == "Хрустящие гренки":
        return 1.00
    else:
        return 0

def extra_dish_tuna(extra):
    if extra == "Креветки":
        return 4.00
    elif extra == "Авокадо":
        return 2.50
    elif extra == "Яйцо":
        return 0.50
    else:
        return 0

def dessert_selection(dessert):
    global dessert_cash, dessert_extra_cash
    if dessert == "Чизкейк":
        dessert_cash = 5
        dessert_extra_change = input("Хотите добавить экстра: Топпинг (шоколадный, карамельный, +1.00€), Орехи (+1.00€), Взбитые сливки (+1.50€)? или Отказаться \n").capitalize()
        dessert_extra_cash = extra_dish_dessert(dessert_extra_change)
        return f"Вы выбрали {dessert}"
    elif dessert == "Маффин":
        dessert_cash = 4
        dessert_extra_change = input("Хотите добавить экстра: Топпинг (шоколадный, карамельный, +1.00€), Орехи (+1.00€), Взбитые сливки (+1.50€)? или Отказаться \n").capitalize()
        dessert_extra_cash = extra_dish_dessert(dessert_extra_change)
        return f"Вы выбрали {dessert}"
    elif dessert == "Тирамису":
        dessert_cash = 6
        dessert_extra_change = input("Хотите добавить экстра: Топпинг (шоколадный, карамельный, +1.00€), Орехи (+1.00€), Взбитые сливки (+1.50€)? или Отказаться \n").capitalize()
        dessert_extra_cash = extra_dish_dessert(dessert_extra_change)
        return f"Вы выбрали {dessert}"
    else:
        return "Вы отказались от заказа десерта!"

def extra_dish_dessert(extra):
    if extra == "Топпинг":
        return 1.00
    elif extra == "Орехи":
        return 1.00
    elif extra == "Взбитые сливки":
        return 1.50
    else:
        return 0

def drink_selection(drink):
    global drink_cash, drink_extra_cash
    if drink == "Кофе":
        drink_cash = 3
        drink_extra_change = input("Хотите добавить экстра: Лед (бесплатно), Фрукты (+2.00€), Мята (+0.80€)? или Отказаться \n").capitalize()
        drink_extra_cash = extra_dish_drink(drink_extra_change)
        return f"Вы выбрали {drink}"
    elif drink == "Чай":
        drink_cash = 2.5
        drink_extra_change = input("Хотите добавить экстра: Лед (бесплатно), Фрукты (+2.00€), Мята (+0.80€)? или Отказаться \n").capitalize()
        drink_extra_cash = extra_dish_drink(drink_extra_change)
        return f"Вы выбрали {drink}"
    elif drink == "Лимонад":
        drink_cash = 4
        drink_extra_change = input("Хотите добавить экстра: Лед (бесплатно), Фрукты (+2.00€), Мята (+0.80€)? или Отказаться \n").capitalize()
        drink_extra_cash = extra_dish_drink(drink_extra_change)
        return f"Вы выбрали {drink}"
    else:
        return "Вы отказались от заказа напитка!"


def extra_dish_drink(extra):
    if extra == "Лед":
        return 0
    elif extra == "Фрукты":
        return 2.00
    elif extra == "Мята":
        return 0.80
    else:
        return 0


def finalize_order():
    total_price = main_course_cash + main_course_extra_cash + salad_cash + salad_extra_cash + dessert_cash + dessert_extra_cash + drink_cash + drink_extra_cash
    print("\nВаш заказ:")
    print(f"Основное блюдо: {main_course_cash}€ + {main_course_extra_cash}€")
    print(f"Салат: {salad_cash}€ + {salad_extra_cash}€")
    print(f"Десерт: {dessert_cash}€ + {dessert_extra_cash}€")
    print(f"Напиток: {drink_cash}€ + {drink_extra_cash}€")
    print(f"Общая стоимость: {total_price}€")
    print("Всё верно? Если хотите что-то изменить, напишите номер позиции:")
    print("1. Основное блюдо")
    print("2. Салат")
    print("3. Десерт")
    print("4. Напиток")
    print("5. Всё верно")

    choice = input().strip()
    if choice == "1":
        main_dish = input("Выберите основное блюдо: Пицца / Паста / Стейк: или Отказаться\n").capitalize()
        main_course(main_dish)
    elif choice == "2":
        salad = input("Выберите салат: Цезарь / Греческий / Салат с тунцом: или Отказаться\n").capitalize()
        salad_selection(salad)
    elif choice == "3":
        dessert = input("Выберите десерт: Чизкейк / Маффин / Тирамису: или Отказаться\n").capitalize()
        dessert_selection(dessert)
    elif choice == "4":
        drink = input("Выберите напиток: Кофе / Чай / Лимонад: или Отказаться\n").capitalize()
        drink_selection(drink)
    elif choice == "5":
        print("\nКстати, у нас сегодня новые маффины с карамельной начинкой за 3.50€. Добавим?")
        extra_dessert = input().strip().lower()
        if extra_dessert == "да":
            print("Ваш окончательный заказ:")
            print(f"Основное блюдо: {main_course_cash}€ + {main_course_extra_cash}€")
            print(f"Салат: {salad_cash}€ + {salad_extra_cash}€")
            print(f"Десерт: {dessert_cash}€ + {dessert_extra_cash}€")
            print(f"Напиток: {drink_cash}€ + {drink_extra_cash}€")
            print("Маффин с карамельной начинкой - 3.50€")
            total_price += 3.50
            print(f"Общая стоимость: {total_price}€")
        else:
            print("Ваш окончательный заказ:")
            print(f"Основное блюдо: {main_course_cash}€ + {main_course_extra_cash}€")
            print(f"Салат: {salad_cash}€ + {salad_extra_cash}€")
            print(f"Десерт: {dessert_cash}€ + {dessert_extra_cash}€")
            print(f"Напиток: {drink_cash}€ + {drink_extra_cash}€")
            print(f"Общая стоимость: {total_price}€")
        print("Спасибо за заказ! Ожидайте доставку через 30 минут. Хорошего дня!")
    else:
        print("Некорректный выбор. Попробуйте снова.")
        finalize_order()


print("Привет! Я помогу вам оформить заказ. Давайте начнем с выбора основного блюда.")
main_dish = input("Выберите основное блюдо:\n1. Пицца\n2. Паста\n3. Стейк\n4. Отказаться\n").capitalize()
main_course(main_dish)
print("Отлично! Теперь выберите салат:")
salad = input("Выберите салат: Цезарь / Греческий / Салат с тунцом: или Отказаться\n").capitalize()
salad_selection(salad)
print("Прекрасный выбор! Теперь выберите десерт:")
dessert = input("Выберите десерт: Чизкейк / Маффин / Тирамису: или Отказаться\n").capitalize()
dessert_selection(dessert)
print("Замечательно! Теперь выберите напиток:")
drink = input("Выберите напиток: Кофе / Чай / Лимонад: или Отказаться\n").capitalize()
drink_selection(drink)
finalize_order()
