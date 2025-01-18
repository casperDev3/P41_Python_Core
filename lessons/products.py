# Підключаємо бібліотеку requests для роботи з HTTP запитами
import requests

# Задаємо базовий URL для API, який буде використовуватися для отримання продуктів
BASE_URL = "https://fakestoreapi.com"

# Виводимо вітальне повідомлення
print("Welcome to the Fake Store API")
print("Start getting products...\n")

# Виконуємо GET запит до API за допомогою бібліотеки requests
# та отримуємо список продуктів
products = requests.get(f"{BASE_URL}/products").json()

# Виводимо повідомлення про успішне завершення отримання продуктів
print("Products were fetched successfully!")
print("Products:\n" )

# Виводимо список продуктів
print(products)

### Домашнє завдання
'''Д/з: 
1. Потрібно відобразити всі продукти дешевше 100 грн
2. Відобразити всі товари з категорії електроніка
3. Розташувати всі товари в алфавітному порядку (**за бажанням)
'''

### Рекомендації до виконання домашнього завдання:
# Для виконання цих завдань потрібно використати медом filter() та метод sort()

### Приклади:
'''
# Відфільтрувати товари з категорії "men's clothing"
men_clothing = list(filter(lambda x: x['category'] == "men's clothing", products))

# Відсортувати від найдорожчого до найдешевшого
sorted_men_clothing = sorted(men_clothing, key=lambda x: x['price'], reverse=True)

print(sorted_men_clothing)
'''


