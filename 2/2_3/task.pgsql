-- DROP TABLE "level" CASCADE;
-- DROP TABLE "employees" CASCADE;
-- DROP TABLE "department" CASCADE;
-- DROP FUNCTION "department_quantity";
-- DROP TABLE "assessment_mark" CASCADE;
-- DROP TABLE "assessment" CASCADE;

-- 1. Создать таблицу с основной информацией о сотрудниках: 
-- 	ФИО, 
-- 	дата рождения, 
-- 	дата начала работы, 
-- 	должность, 
-- 	уровень сотрудника (jun, middle, senior, lead), 
-- 	уровень зарплаты, 
-- 	идентификатор отдела, 
-- 	наличие/отсутствие прав(True/False).
-- При этом в таблице обязательно должен быть уникальный номер для каждого сотрудника.

CREATE TABLE "level"(			-- Таблица уровеня сотрудника (jun - 1, middle - 2, senior - 3, lead - 4)
	id				serial PRIMARY KEY,	-- id уровня
	title			text NOT NULL 		-- Название уровня 
);
INSERT INTO "level" (title) VALUES
	('jun'),
	('middle'),
	('senior'),
	('lead');
CREATE TABLE "employees"(		-- Таблица сотрудников
	id				serial PRIMARY KEY,	-- id сотрудника
	fio				text,				-- ФИО
	birth 			date, 				-- Дата рождения
	work_start 		date, 				-- Дата начала работы
	post			varchar(80),		-- Должность
	id_level		int,	  			-- Уровень сотрудника (jun - 1, middle - 2, senior - 3, lead - 4)
	salary			int,				-- Зарплата
	id_department	int,				-- id отдела
	driving			boolean,			-- наличие/отсутствие водительских прав(True/False)
	FOREIGN KEY (id_level) REFERENCES "level" (id) ON DELETE SET NULL ON UPDATE CASCADE
);

--   2. Для будущих отчетов аналитики попросили вас создать еще одну таблицу с информацией по отделам.
--   В таблице должено быть: 
--   	идентификатор для каждого отдела, 
-- 		название отдела (например. Бухгалтерский или IT отдел), 
-- 		ФИО руководителя,
-- 		количество сотрудников.

CREATE TABLE "department"(		-- Таблица отделов
	id				serial PRIMARY KEY,	-- id отдела
	title			text NOT NULL,		-- название отдела
	id_director		int,				-- ФИО руководителя 
	quantity		int DEFAULT 0,		-- количество сотрудников
	FOREIGN KEY (id_director) REFERENCES "employees" (id) ON DELETE SET NULL ON UPDATE CASCADE
);
-- Примичание: 
-- 	Мне кажется имея список сотрудников лучше вместо 
-- 	вписывания ФИО руководителя указывать его id
ALTER TABLE "employees"  -- добавление вторичного ключа в таблицу сотрудников
    ADD CONSTRAINT employees_id_department_department_id
    FOREIGN KEY (id_department) 
    REFERENCES "department" (id);

CREATE FUNCTION public.department_quantity() -- тригерная функция обновления колличества сотрудников
    RETURNS trigger
    LANGUAGE 'plpgsql'
    VOLATILE
    COST 100
AS $BODY$
BEGIN
	IF (TG_OP = 'INSERT') THEN
		UPDATE department SET quantity = 
		(SELECT count(*) FROM employees WHERE id_department=NEW.id_department)
		WHERE id=NEW.id_department;
	ELSE
		UPDATE department SET quantity = 
		(SELECT count(*) FROM employees WHERE id_department=OLD.id_department)
		WHERE id=OLD.id_department;
	END IF;
	RETURN NEW; 
END;
$BODY$;

CREATE TRIGGER tr_department_quantity -- сам тригер
AFTER INSERT OR DELETE ON "employees" FOR EACH ROW
EXECUTE PROCEDURE department_quantity();
-- Примичание: 
-- 	Пусть колличество сотрудников обновляется самой СУБД через тригернную функцию

-- 3. На кону конец года и необходимо выплачивать сотрудникам премию. Премия будет 
-- выплачиваться по совокупным оценкам, которые сотрудники получают в каждом квартале года.
-- Создайте таблицу, в которой для каждого сотрудника будут его оценки за каждый квартал.
-- Диапазон оценок от A – самая высокая, до E – самая низкая.

CREATE TABLE "assessment_mark"(		-- Таблица названий оценок
	id				serial PRIMARY KEY,	-- id оценки
	mark			text NOT NULL		-- название оценки
);
INSERT INTO "assessment_mark" (mark) VALUES
	('E'),
	('D'),
	('C'),
	('B'),
	('A');

CREATE TABLE "assessment"(		-- Таблица оценок
	id				serial PRIMARY KEY,	-- id
	id_employee		int NOT NULL,		-- id сотрудника
	year			smallint,			-- год кварталов
	quarter_1		int,				-- первый квартал
	quarter_2		int,				-- второй квартал
	quarter_3		int,				-- третий квартал
	quarter_4		int,				-- четвёртый квартал
	FOREIGN KEY (id_employee) REFERENCES "employees" (id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (quarter_1) REFERENCES "assessment_mark" (id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (quarter_2) REFERENCES "assessment_mark" (id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (quarter_3) REFERENCES "assessment_mark" (id) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (quarter_4) REFERENCES "assessment_mark" (id) ON DELETE SET NULL ON UPDATE CASCADE
);

-- 4. Несколько уточнений по предыдущим заданиям – в первой таблице должны быть записи 
-- как минимум о 5 сотрудниках, которые работают как минимум в 2-х разных отделах. 
-- Содержимое соответствующих атрибутов остается на совесть вашей фантазии, но, желательно 
-- соблюдать осмысленность и правильно выбирать типы данных 
-- (для зарплаты – числовой тип, для ФИО – строковый и т.д.)

INSERT INTO "department" (title) VALUES
	('Бухгалтерский отдел'),
	('IT отдел');

INSERT INTO "employees" (fio, birth, work_start, post, id_level, salary, id_department, driving) VALUES
	('Сотрудник1', DATE('1999-01-01'), DATE('2008-01-01'), 'Джуниор программист', 1, 50000, 2, True),
	('Сотрудник2', DATE('1998-01-01'), DATE('2007-01-01'), 'Мидл программист',2, 60000, 2, True),
	('Сотрудник3', DATE('1997-01-01'), DATE('2006-01-01'), 'Тим лид',4, 70000, 2, False),
	('Сотрудник4', DATE('1996-01-01'), DATE('2005-01-01'), 'Главный бухгалтер',NULL, 100000, 1, False),
	('Сотрудник5', DATE('1996-02-02'), DATE('2005-02-02'), 'Помошник бухгалтер',NULL, 90000, 1, True);

UPDATE department SET id_director = 4 WHERE id=1;
UPDATE department SET id_director = 3 WHERE id=2;

INSERT INTO "assessment" (id_employee, year, quarter_1, quarter_2, quarter_3, quarter_4) VALUES
	(1,2009,1,1,1,1),
	(2,2009,2,2,2,2),
	(3,2009,3,3,3,3),
	(4,2009,4,4,4,4),
	(5,2009,5,5,5,5);

-- 5. Ваша команда расширяется и руководство запланировало открыть новый отдел 
-- – отдел Интеллектуального анализа данных. На начальном этапе в команду наняли 
-- одного руководителя отдела и двух сотрудников. Добавьте необходимую информацию 
-- в соответствующие таблицы.

INSERT INTO "department" (title) VALUES
	('Интеллектуального анализа данных');

INSERT INTO "employees" (fio, birth, work_start, post, id_level, salary, id_department, driving) VALUES
	('Сотрудник6', DATE('2000-01-01'), DATE('2009-01-01'), 'Джуниор программист', 1, 70000, 3, True),
	('Сотрудник7', DATE('2001-01-01'), DATE('2009-01-01'), 'Джуниор программист',2, 70000, 3, True),
	('Сотрудник8', DATE('2002-01-01'), DATE('2009-01-01'), 'Тим лид',4, 80000, 3, False);

UPDATE department SET id_director = 4 WHERE id=8;

INSERT INTO "assessment" (id_employee, year, quarter_1, quarter_2, quarter_3, quarter_4) VALUES
	(6,2009,3,3,3,3),
	(7,2009,4,4,4,4),
	(8,2009,5,5,5,5);

-- 6. Теперь пришла пора анализировать наши данные – напишите запросы для получения следующей информации:
--		Уникальный номер сотрудника, его ФИО и стаж работы – для всех сотрудников компании
--		Уникальный номер сотрудника, его ФИО и стаж работы – только первых 3-х сотрудников
--		Уникальный номер сотрудников - водителей
--		Выведите номера сотрудников, которые хотя бы за 1 квартал получили оценку D или E
--		Выведите самую высокую зарплату в компании.

-- Уникальный номер сотрудника, его ФИО и стаж работы – для всех сотрудников компании
SELECT id, fio, date_part('year',age(NOW(),work_start)) AS experience FROM "employees";

-- Уникальный номер сотрудника, его ФИО и стаж работы – только первых 3-х сотрудников
SELECT id, fio, date_part('year',age(NOW(),work_start)) AS experience FROM "employees" LIMIT 3;

-- Уникальный номер сотрудников - водителей
SELECT id FROM "employees" WHERE driving=true;

-- Выведите номера сотрудников, которые хотя бы за 1 квартал получили оценку D или E
SELECT employees.id FROM employees
LEFT JOIN assessment ON employees.id = assessment.id_employee
LEFT JOIN assessment_mark AS q1 ON q1.id = assessment.quarter_1
LEFT JOIN assessment_mark AS q2 ON q2.id = assessment.quarter_2
LEFT JOIN assessment_mark AS q3 ON q3.id = assessment.quarter_3
LEFT JOIN assessment_mark AS q4 ON q4.id = assessment.quarter_4
WHERE q1.mark = 'D' OR q1.mark = 'E' 
   OR q2.mark = 'D' OR q2.mark = 'E' 
   OR q3.mark = 'D' OR q3.mark = 'E' 
   OR q4.mark = 'D' OR q4.mark = 'E';

-- Выведите самую высокую зарплату в компании.
SELECT MAX(salary) FROM employees;
