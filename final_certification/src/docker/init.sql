CREATE DATABASE project;
GRANT ALL PRIVILEGES ON DATABASE project TO airflow;
\c project;

CREATE TABLE level(			            -- Таблица уровеня сотрудника (jun - 1, middle - 2, senior - 3, lead - 4)
	id				serial PRIMARY KEY,	-- id уровня
	title			text NOT NULL 		-- Название уровня 
);