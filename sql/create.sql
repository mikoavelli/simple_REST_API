CREATE TABLE planets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    discovered_date DATE
);

CREATE TABLE governments (
    id SERIAL PRIMARY KEY,
    planet_id INTEGER UNIQUE REFERENCES planets(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL,
    leader VARCHAR(100),
    established_date DATE
);

CREATE TABLE states (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    planet_id INTEGER REFERENCES planets(id) ON DELETE CASCADE,
    population INTEGER,
    area FLOAT,
    UNIQUE (name, planet_id)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state_id INTEGER REFERENCES states(id) ON DELETE CASCADE,
    population INTEGER,
    founded_date DATE
);