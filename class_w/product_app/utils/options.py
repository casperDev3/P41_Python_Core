from class_w.product_app.helpers.main import h_menu
from .quiz import age_quiz
from .converter import converter
from .products import Product

def menu_opt(ch):
    if ch == 0:
        for i in range(1, 10000, 1):
            print(f"SPAM----{i}")
            continue
        return h_menu(action="active", msg="SPAM")
    elif ch == 1:
        age_quiz()
        return h_menu(action="active", msg="Вікова вікторина")
    elif ch == 2:
        converter()
        return h_menu(action="active", msg="Option 2")
    elif ch == 3:
        product = Product("Phone", 1000)
        print(product)
        return h_menu(action="active", msg="Option 3")
    elif ch == 4:
        print("Опція 4")
        return h_menu(action="active", msg="Option 4")
    elif ch == 5:
        print("До побачення!")
        return h_menu(status=False, action="exit", msg="Exit")
    else:
        print("Виберіть опцію від 1 до 5")
        return h_menu(status=False, action="continue", msg="Continue")

    # Завдання: Додати новий пункт меню для квізу про аніме
    #
    # Опис завдання:
    # Уявіть, що ви створюєте додаток з меню, яке містить кілька розділів.
    # Ваше завдання - додати четвертий пункт меню, який буде називатися "Квіз про аніме".
    # Після вибору цього пункту, користувачеві повинно виводитися повідомлення
    # про початок квізу, наприклад: "Вітаємо у квізі про аніме! Відповідайте на питання!"
    #
    # Вимоги:
    # 1. Додати четвертий пункт у список меню.
    # 2. Реалізувати вибір цього пункту через введення користувачем числа.
    # 3. Якщо користувач обирає цей пункт, вивести відповідне повідомлення.
    #
    # Підказка: Використовуйте списки, цикли та умовні конструкції для реалізації меню.

    # Напишіть код нижче:

