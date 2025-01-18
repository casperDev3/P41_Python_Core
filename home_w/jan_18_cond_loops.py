# Імпортуємо бібліотеку для кольору тексту (не обов'язково, але додає колорит)
from colorama import init, Fore
init(autoreset=True)

# Словник з питаннями та відповідями
questions = {
    "Наруто": [
        {"question": "Хто є головним героєм в \"Наруто\"?",
         "options": ["Саске", "Наруто", "Какаші"],
         "answer": "Наруто"},
        {"question": "Яке село є домом для Наруто?",
         "options": ["Село Прихованого Листя", "Село Прихованого Піску", "Село Прихованого Туману"],
         "answer": "Село Прихованого Листя"}
    ],
    "Атака Титанів": [
        {"question": "Хто є найвищим титаном в \"Атака Титанів\"?",
         "options": ["Колосальний Титан", "Броньований Титан", "Жіночий Титан"],
         "answer": "Колосальний Титан"},
        {"question": "Хто володіє силою титана в середині сюжету?",
         "options": ["Ерен Єгер", "Мікса Аккерман", "Армін Арлерт"],
         "answer": "Ерен Єгер"}
    ],
    "Мій сусід Тоторо": [
        {"question": "Яке магічне істота є в \"Мій сусід Тоторо\"?",
         "options": ["Дракон", "Тоторо", "Фея"],
         "answer": "Тоторо"},
        {"question": "Скільки сестер головних героїв у фільмі?",
         "options": ["Одна", "Дві", "Три"],
         "answer": "Дві"}
    ]
}

# START GAME
print(Fore.GREEN + "Вітаю вас у грі \"Вгадай аніме\"!")



#### ПРИКЛАД ВИКОРИСТАННЯ ДОМАШНЬОГО ЗАВДАННЯ ####
# from colorama import init, Fore
# init(autoreset=True)
#
# # Словник з питаннями та відповідями про супергероїв
# questions = {
#     "Marvel": [
#         {"question": "Хто є головним супергероєм у всесвіті Marvel?",
#          "options": ["Бетмен", "Супермен", "Залізна Людина"],
#          "answer": "Залізна Людина"},
#         {"question": "Який супергерой має здатність змінювати час?",
#          "options": ["Флеш", "Тор", "Доктор Стрендж"],
#          "answer": "Доктор Стрендж"}
#     ],
#     "DC": [
#         {"question": "Хто є найбільш відомим супергероєм у всесвіті DC?",
#          "options": ["Бетмен", "Аквамен", "Зелений Ліхтар"],
#          "answer": "Бетмен"},
#         {"question": "Хто є головним антагоністом для Бетмена?",
#          "options": ["Лекс Лютор", "Джокер", "Доктор Октопус"],
#          "answer": "Джокер"}
#     ]
# }
#
# # Початковий рахунок
# score = 0
#
# # Основний цикл квізу
# for universe, quiz in questions.items():
#     print(f"\n{Fore.GREEN}Тема: {universe}{Fore.RESET}")
#     for question_data in quiz:
#         print(question_data["question"])
#         for i, option in enumerate(question_data["options"], 1):
#             print(f"{i}. {option}")
#
#         # Запит відповіді від користувача
#         answer = input("Введіть номер правильної відповіді: ")
#
#         # Перевірка відповіді
#         if question_data["options"][int(answer) - 1] == question_data["answer"]:
#             print(f"{Fore.GREEN}Правильно!{Fore.RESET}")
#             score += 1
#         else:
#             print(f"{Fore.RED}Неправильно! Правильна відповідь була: {question_data['answer']}{Fore.RESET}")
#
# # Вивід фінального рахунку
# total_questions = sum(len(quiz) for quiz in questions.values())
# print(f"\nВаш фінальний бал: {score}/{total_questions}")