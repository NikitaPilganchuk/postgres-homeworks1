-- Напишите запросы, которые выводят следующую информацию:
-- 1. "имя контакта" и "город" (contact_name, city) из таблицы customers (только эти две колонки)
SELECT contact_name, city from customers

-- 2. идентификатор заказа и разницу между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
SELECT order_id,shipped_date - order_date as column from orders

-- 3. все города без повторов, в которых зарегистрированы заказчики (customers)
SELECT DISTINCT ship_city from orders

-- 4. количество заказов (таблица orders)
SELECT count(order_id) from orders

-- 5. количество стран, в которые отгружался товар (таблица orders, колонка ship_country)
SELECT Count(Distinct(ship_country)) from orders