"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

data_folder = 'C:\\Users\\User\\Desktop\\postgres-homeworks1\\homework-1\\north_data'
connection = psycopg2.connect(
    host="localhost",
    database='north',
    user='postgres',
    password='A5A4A3a2a1'
)

# создание курсора
cursor = connection.cursor()

# Заполнение таблицы customers
customers_file = os.path.join(data_folder, 'customers_data.csv')
with open(customers_file, 'r', encoding='utf-8') as file:
    next(file)
    for line in file:
        line = line.strip().split(',')
        customer_id, company_name, contact_name = line
        cursor.execute('INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)',
                       (customer_id, company_name, contact_name))

# Заполнение таблицы employees
employees_file = os.path.join(data_folder, 'employees_data.csv')
with open(employees_file, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for line in csvreader:
        employee_id=line[0]
        first_name=line[1]
        last_name=line[2]
        title=line[3]
        birth_date=line[4]
        notes=line[5]
        cursor.execute(
            'INSERT INTO employees (employee_id,first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)',
            (employee_id, first_name, last_name, title, birth_date, notes))

# Заполнение таблицы orders
orders_file = os.path.join(data_folder, 'orders_data.csv')
with open(orders_file, 'r', encoding='utf-8') as file:
    next(file)
    for line in file:
        line = line.strip().split(',')
        order_id, customer_id, employee_id, order_date, ship_city = line
        cursor.execute(
            'INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)',
            (order_id, customer_id, employee_id, order_date, ship_city))

    # Сохранение изменений
    connection.commit()

    # Закрытие подключения
    cursor.close()
    connection.close()
