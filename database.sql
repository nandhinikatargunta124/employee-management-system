CREATE DATABASE employee_management;

USE employee_management;

CREATE TABLE employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(50),
    salary INT,
    joining_date DATE
);
