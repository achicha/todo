-- create all Database tables from this file

-- delete old tables
DROP TABLE IF EXISTS posts;

-- posts table
CREATE TABLE IF NOT EXISTS posts (id SERIAL PRIMARY KEY, text CHAR(300), date_posted DATE);
