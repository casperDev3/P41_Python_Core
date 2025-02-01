from colorama import Fore

def age_quiz():
    print("Вікова вікторина")
    questions = {
        "Зумери": [
            {"question": "Що означає 'yeet'?",
             "options": ["Вітаю", "Викидаю/кидаю", "Люблю"],
             "answer": "Викидаю/кидаю"},
            {"question": "Як зумери називають 'роботу'?",
             "options": ["Халепа", "Гайка", "Грінда"],
             "answer": "Грінда"}
        ],
        "Бумери": [
            {"question": "Що означає 'дискета'?",
             "options": ["USB-накопичувач", "Зовнішній жорсткий диск",
                         "Знімний носій даних у вигляді квадратної пластикової коробки"],
             "answer": "Знімний носій даних у вигляді квадратної пластикової коробки"},
            {"question": "Як бумери можуть назвати 'інтернет'?",
             "options": ["Всесвітня павутина", "Глобальна система", "Телеграф"],
             "answer": "Всесвітня павутина"}
        ],
        "Альфа": [
            {"question": "Що означає 'roblox'?",
             "options": ["Тип ігор", "Нова марка одягу", "Вид музики"],
             "answer": "Тип ігор"},
            {"question": "Як покоління Альфа може називати 'книги'?",
             "options": ["Паперові сторінки", "Сторінки", "Екрани з текстом"],
             "answer": "Паперові сторінки"}
        ]
    }

    # START GAME
    print(Fore.GREEN + "Вітаю вас у грі \"Вгадай слово з епохи\"!")

    while True:
        # Виводимо список епох
        print(Fore.YELLOW + "Виберіть епоху:"
                            "\n1. Вікторина")
        print(Fore.RED + "0. Вихід\n")

        # Вибір епохи
        action = int(input(Fore.BLUE + "Ваш вибір: "))

        # Перевірка на вибір
        if action == 1:
            open_main_menu = False
            for universe, quiz in questions.items():
                print(f"\n{Fore.GREEN}Тема: {universe}{Fore.RESET}")
                for question_data in quiz:
                    print(question_data["question"])
                    for i, option in enumerate(question_data["options"], 1):
                        print(f"{i}. {option}")

                    # Запит відповіді від користувача
                    print(Fore.RED + "\n0. Вийти в голоне меню")
                    answer = input("Введіть номер правильної відповіді: ")
                    if answer == "0":
                        open_main_menu = True
                        break

                    # Перевірка відповіді
                    if question_data["options"][int(answer) - 1] == question_data["answer"]:
                        print(f"{Fore.GREEN}Правильно!{Fore.RESET}\n")
                    else:
                        print(
                            f"{Fore.RED}Неправильно! Правильна відповідь була: {question_data['answer']}{Fore.RESET}\n")
                if open_main_menu:
                    break

        elif action == 0:
            print(Fore.RED + "Дякую за гру!")
            break
        else:
            print(Fore.RED + "Виберіть доступну опцію!")
            continue
