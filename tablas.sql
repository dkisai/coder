
-- Tabla de países
CREATE TABLE countries (
    id INT PRIMARY KEY,
    name VARCHAR(30)
);

-- Tabla de idiomas hablados
CREATE TABLE spoken_languages (
    id INT PRIMARY KEY,
    english_name VARCHAR(30),
    iso_639_1 VARCHAR(3),
    name VARCHAR(30)
);

-- Tabla de películas
CREATE TABLE movies (
    id INT PRIMARY KEY,
    title VARCHAR(350),
    original_title VARCHAR(350),
    release_date DATE,
    poster_path VARCHAR(100),
    overview TEXT,
    budget INT,
    revenue INT,
    runtime SMALLINT,
    tagline TEXT
);

-- Tabla intermedia para géneros de películas
CREATE TABLE movie_genres (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies (id),
    FOREIGN KEY (genre_id) REFERENCES genres (id)
);

-- Tabla intermedia para países de películas
CREATE TABLE movie_countries (
    movie_id INT,
    country_id INT,
    PRIMARY KEY (movie_id, country_id),
    FOREIGN KEY (movie_id) REFERENCES movies (id),
    FOREIGN KEY (country_id) REFERENCES countries (id)
);

-- Tabla intermedia para idiomas hablados de películas
CREATE TABLE movie_spoken_languages (
    movie_id INT,
    spoken_language_id INT,
    PRIMARY KEY (movie_id, spoken_language_id),
    FOREIGN KEY (movie_id) REFERENCES movies (id),
    FOREIGN KEY (spoken_language_id) REFERENCES spoken_languages (id)
);

CREATE TABLE overview (
    id INT PRIMARY KEY,
    overview TEXT,
    FOREIGN KEY (id) REFERENCES movies (id)
);