import os
import json
from collections import Counter

# Указываем путь к файлу
file_path = r"C:\Users\nataz\Downloads\orders_july_2023.json.json"  # Убрано двойное расширение

# Проверяем наличие файла
if not os.path.exists(file_path):
    print(f"Файл не найден: {file_path}")
    # Выводим список файлов в папке, если файл не найден
    downloads_path = r"C:\Users\nataz\Downloads"
    print("Список файлов в каталоге:", os.listdir(downloads_path))
else:
    # Считываем данные из файла
    with open(file_path, "r") as file:
        orders = json.load(file)

    # Переменные для анализа данных
    max_price = 0
    max_order_price = ''

    max_items = 0
    max_order_items = ''

    orders_per_day = Counter()
    user_orders = Counter()
    user_total_spent = Counter()

    total_price = 0
    total_orders = 0
    total_items = 0

    # Обрабатываем данные
    for order_num, order_data in orders.items():
        date = order_data['date']
        user_name = order_data['user_id']
        items_count = order_data['quantity']
        price = order_data['price']

        # Находим максимальную цену заказа
        if price > max_price:
            max_price = price
            max_order_price = order_num

        # Находим заказ с максимальным количеством товаров
        if items_count > max_items:
            max_items = items_count
            max_order_items = order_num

        # Считаем заказы и траты по пользователям
        user_orders[user_name] += 1
        user_total_spent[user_name] += price

        # Считаем заказы по дням
        orders_per_day[date] += 1

        # Общая статистика
        total_price += price
        total_orders += 1
        total_items += items_count

    # Вывод результатов
    print(f"Самый дорогой заказ: {max_order_price} на сумму {max_price}")
    print(f"Заказ с наибольшим количеством товаров: {max_order_items}, {max_items} товаров")
    print(f"Средняя стоимость заказа: {total_price / total_orders:.2f}")
    print(f"Среднее количество товаров в заказе: {total_items / total_orders:.2f}")
    print(f"Количество заказов по дням: {dict(orders_per_day)}")
    print(f"Пользователи и количество их заказов: {dict(user_orders)}")
    print(f"Пользователи и их траты: {dict(user_total_spent)}")


