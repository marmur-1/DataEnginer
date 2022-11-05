-- 1. Чтобы успешно справиться с данным практическим заданием, вам необходимо выполнить как минимум задания 1-4 практики 
-- в теме 2.3 "Реляционные базы данных: PostgreSQL", но желательно сделать, конечно же, все.
-- 2. Теперь мы знакомы с гораздо большим перечнем операторов языка SQL и это дает нам дополнительные возможности для 
-- анализа данных. Выполните следующие запросы:

-- a. Попробуйте вывести не просто самую высокую зарплату во всей команде,
-- а вывести именно фамилию сотрудника с самой высокой зарплатой.
SELECT fio,salary
FROM employees 
WHERE salary = (SELECT MAX(salary) FROM employees);

-- b. Попробуйте вывести фамилии сотрудников в алфавитном порядке
SELECT fio
FROM employees 
ORDER BY fio;

-- c. Рассчитайте средний стаж для каждого уровня сотрудников
SELECT level.title AS level, AVG(date_part('year',age(NOW(),employees.work_start))) AS experience 
FROM employees
LEFT JOIN level ON employees.id_level = level.id
GROUP BY level;

-- d. Выведите фамилию сотрудника и название отдела, в котором он работает
SELECT employees.fio, department.title
FROM employees
LEFT JOIN department ON department.id = employees.id_department;

-- e. Выведите название отдела и фамилию сотрудника с самой высокой зарплатой 
-- в данном отделе и саму зарплату также.
SELECT b.title AS department_title,
       e.fio,
       d.max AS salary
FROM employees AS e
RIGHT JOIN (
    SELECT id_department, MAX(salary)
    FROM employees
    GROUP BY id_department
) AS d ON e.id_department = d.id_department 
      AND e.salary = d.max
LEFT JOIN department AS b ON b.id = d.id_department  



