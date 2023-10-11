CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date DATE,
	notes text
);


CREATE TABLE customers
(
	customer_id varchar(6) NOT NULL,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(6) NOT NULL,
	employee_id int,
	order_date DATE,
	ship_city varchar(100)
);-- SQL-команды для создания таблиц
