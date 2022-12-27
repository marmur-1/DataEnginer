CREATE DATABASE project;
GRANT ALL PRIVILEGES ON DATABASE project TO airflow;
\c project;

CREATE TABLE IF NOT EXISTS tickets(			-- Таблица тикетов валюты
	symbol			text NOT NULL, 		-- символ акции
	timestamp		timestamp NOT NULL,	-- дата и время тикета
	id_day			text,               	-- сурогатный ключ категории        
	open			float,			-- цена открытия
	close			float,			-- цена закрытия
	high			float,			-- максимальная цена
	low			float,			-- минимальная цена
	volume			int,			-- колличество торгов
	PRIMARY KEY (symbol, timestamp)
);

CREATE FUNCTION public.tickets_id_day() 		-- тригерная функция добавления сурогатного ключа
	RETURNS trigger
	LANGUAGE 'plpgsql'
	VOLATILE
	COST 100
AS $BODY$
BEGIN
	NEW.id_day := concat(NEW.timestamp::date,'_',NEW.symbol);
	RETURN NEW;
END
$BODY$;

CREATE TRIGGER tickets_id_day           		-- сам тригер
BEFORE INSERT ON tickets FOR EACH ROW
EXECUTE PROCEDURE public.tickets_id_day();

CREATE TABLE IF NOT EXISTS days_analytics(          	-- Таблица аналитики дня
	id_day			text NOT NULL PRIMARY KEY,-- Суррогатный ключ категории    
	symbol			text NOT NULL, 		-- Название валюты
	sum_volume		int,			-- Суммарный объем торгов за последние сутки
	day_open		float,			-- Курс валюты на момент открытия торгов для данных суток
	day_close		float,			-- Курс валюты на момент закрытия торгов для данных суток
	relative_op		float,			-- Разница(в %) курса с момента открытия до момента закрытия торгов для данных суток
	max_volume_interval 	timestamp,		-- Минимальный временной интервал, на котором был зафиксирован самый крупный объем торгов для данных суток
	max_price_interval	timestamp,		-- Минимальный временной интервал, на котором был зафиксирован максимальный курс для данных суток
	min_price_interval	timestamp		-- Минимальный временной интервал, на котором был зафиксирован минимальный курс торгов для данных суток
);
