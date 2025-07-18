CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2),
    department_id INT,
    email VARCHAR(255),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- insert random data for output
INSERT INTO departments (department_id, name, location) VALUES
(1, 'Engineering', 'New York'),
(2, 'Sales', 'Chicago'),
(3, 'HR', 'San Francisco'),
(4, 'Finance', 'Boston'),
(5, 'Marketing', 'Los Angeles');


INSERT INTO employees (employee_id, name, salary, department_id, email) VALUES
(101, 'Alice Johnson', 75000.00, 1, 'alice.johnson@example.com'),
(102, 'Bob Smith', 68000.00, 2, 'bob.smith@example.com'),
(103, 'Carol Davis', 85000.00, 1, 'carol.davis@example.com'),
(104, 'David Lee', 56000.00, 3, 'david.lee@example.com'),
(105, 'Eva Brown', 91000.00, 4, 'eva.brown@example.com'),
(106, 'Frank Miller', 72000.00, 5, 'frank.miller@example.com'),
(107, 'Grace Kim', 63000.00, 2, 'grace.kim@example.com'),
(108, 'Henry Wilson', 67000.00, 3, 'henry.wilson@example.com'),
(109, 'Isla Thompson', 80000.00, 1, 'isla.thompson@example.com'),
(110, 'Jack Martinez', 88000.00, 4, 'jack.martinez@example.com');

INSERT INTO employees (employee_id, name, salary, department_id, email) VALUES
(111, 'Isla Thompson Repeat', 85000.00, 1, 'isla.thompson@example.com');


-- GIVEN A DATABASE WITH THE ABOVE TABLES:
-- 1. Find the average salary of all employees.
-- 2. Find the details of employees whose salary is greater than the average salary of employees in the 'HR'
-- department.
-- 3. Find the details of employees whose email address is used by more than one employee.
-- 4. Find employees who earn more than their department's average salary.

-- ans 1
select avg(salary) from employees;

-- ans 2
with hr_avg_salary as (
    select avg(salary) avg_salary from employees e inner join departments d on e.department_id = d.department_id where d.name = 'HR'
)
select * from employees where salary > (select avg_salary from hr_avg_salary)

-- ans 3
with email_used_count as (
    select email,count(employee_id) used_count from employees group by email
)
select e.* from employees e inner join email_used_count euc on e.email = euc.email where used_count > 1;

-- ans 4
with avg_salary_department_wise as (
    select department_id, avg(salary) dep_avg_salary from employees group by department_id
)
select e.* from employees e inner join avg_salary_department_wise asdw on asdw.department_id = e.department_id where e.salary > asdw.dep_avg_salary

