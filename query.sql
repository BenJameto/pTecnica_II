-- query.sql
CREATE TABLE IF NOT EXISTS motos (
    id SERIAL PRIMARY KEY,
    marca VARCHAR(50),
    nombre VARCHAR(50),
    cilindrada INT,
    UNIQUE (marca, nombre, cilindrada)
);
