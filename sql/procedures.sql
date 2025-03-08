CREATE OR REPLACE PROCEDURE add_planet(
    p_name VARCHAR(100),
    p_description TEXT,
    p_discovered_date DATE
)
    LANGUAGE plpgsql
AS
$$
BEGIN
    INSERT INTO planets (name, description, discovered_date)
    VALUES (p_name, p_description, p_discovered_date);
END;
$$;


CREATE OR REPLACE PROCEDURE update_planet(
    p_id INTEGER,
    p_name VARCHAR(100),
    p_description TEXT,
    p_discovered_date DATE
)
    LANGUAGE plpgsql
AS
$$
BEGIN
    UPDATE planets
    SET name            = p_name,
        description     = p_description,
        discovered_date = p_discovered_date
    WHERE id = p_id;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_planet(
    p_id INTEGER
)
    LANGUAGE plpgsql
AS
$$
BEGIN
    DELETE
    FROM planets
    WHERE id = p_id;
END;
$$;


CREATE OR REPLACE PROCEDURE add_government(
    p_planet_id INTEGER,
    p_type VARCHAR(50),
    p_leader VARCHAR(100),
    p_established_date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO governments (planet_id, type, leader, established_date)
    VALUES (p_planet_id, p_type, p_leader, p_established_date);
END;
$$;

CREATE OR REPLACE PROCEDURE update_government(
    p_id INTEGER,
    p_planet_id INTEGER,
    p_type VARCHAR(50),
    p_leader VARCHAR(100),
    p_established_date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE governments
    SET planet_id = p_planet_id,
        type = p_type,
        leader = p_leader,
        established_date = p_established_date
    WHERE id = p_id;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_government(
    p_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM governments
    WHERE id = p_id;
END;
$$;

CREATE OR REPLACE PROCEDURE add_state(
    p_name VARCHAR(100),
    p_planet_id INTEGER,
    p_population INTEGER,
    p_area FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO states (name, planet_id, population, area)
    VALUES (p_name, p_planet_id, p_population, p_area);
END;
$$;

CREATE OR REPLACE PROCEDURE update_state(
    p_id INTEGER,
    p_name VARCHAR(100),
    p_planet_id INTEGER,
    p_population INTEGER,
    p_area FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE states
    SET name = p_name,
        planet_id = p_planet_id,
        population = p_population,
        area = p_area
    WHERE id = p_id;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_state(
    p_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM states
    WHERE id = p_id;
END;
$$;

CREATE OR REPLACE PROCEDURE add_city(
    p_name VARCHAR(100),
    p_state_id INTEGER,
    p_population INTEGER,
    p_founded_date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO cities (name, state_id, population, founded_date)
    VALUES (p_name, p_state_id, p_population, p_founded_date);
END;
$$;

CREATE OR REPLACE PROCEDURE update_city(
    p_id INTEGER,
    p_name VARCHAR(100),
    p_state_id INTEGER,
    p_population INTEGER,
    p_founded_date DATE
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE cities
    SET name = p_name,
        state_id = p_state_id,
        population = p_population,
        founded_date = p_founded_date
    WHERE id = p_id;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_city(
    p_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM cities
    WHERE id = p_id;
END;
$$;