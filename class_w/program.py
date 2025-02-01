from colorama import init, Fore

print(Fore.GREEN + "Програма запущена!\n")
while True:
    # Виводимо меню опцій
    print(Fore.BLUE + "Виберіть опцію:")
    print(Fore.BLUE + "0. Почати СПАМ")
    print(Fore.BLUE + "1. Вивести всі продукти")
    print(Fore.BLUE + "2. Вивести продукти дешевше 100 грн")
    print(Fore.BLUE + "3. Вивести продукти з категорії електроніка")
    print(Fore.BLUE + "4. Вивести продукти в алфавітному порядку")
    print(Fore.RED + "5. Вийти з програми")

    # Отримуємо вибір користувача
    user_input = int(input(Fore.YELLOW + "\nВведіть опцію: "))

    # Перевіряємо вибір користувача
    if user_input == 0:
        for i in range(1, 10000, 1):
            print(f"SPAM----{i}")
            continue
        continue
    elif user_input == 1:
        print("Опція 1")
    elif user_input == 2:
        print("Опція 2")
    elif user_input == 3:
        print("Опція 3")
    elif user_input == 4:
        print("Опція 4")
    elif user_input == 5:
        print("До побачення!")
        break
    else:
        print("Виберіть опцію від 1 до 5")
        continue