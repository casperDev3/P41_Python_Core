from colorama import init, Fore
from items.welcome import welcome_msg
from items.menu import show_menu
from utils.options import menu_opt

# PROGRAM FLOW
# 1. Вивести привітання
welcome_msg()

while True:
    # 2. Вивести меню опцій
    show_menu()

    # 3.  Отримуємо вибір користувача
    user_input = int(input(Fore.YELLOW + "\nВведіть опцію: "))

    # 4. Перевіряємо вибір користувача
    ch_result = menu_opt(user_input)
    if not ch_result['status']:
        if ch_result['action'] == "exit":
            break
        continue
