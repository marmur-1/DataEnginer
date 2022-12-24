CREATE DATABASE project;
GRANT ALL PRIVILEGES ON DATABASE project TO airflow;
\c project;

CREATE TABLE tickets(			        -- Таблица тикетов валюты
	id				text NOT NULL PRIMARY KEY, --id
	symbol			text NOT NULL, 		-- символ акции
	timestamp		timestamp NOT NULL,	-- дата и время тикета
	open			float,				-- цена открытия
    close			float,				-- цена закрытия
    high			float,				-- максимальная цена
    low				float,				-- минимальная цена
    volume			int					-- колличество торгов
);