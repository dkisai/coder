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

CREATE TABLE overviews (
    id INT PRIMARY KEY,
    overview CHARACTER VARYING(5000),
    FOREIGN KEY (id) REFERENCES movies (id)
);

CREATE TABLE genres (
    id INT PRIMARY KEY,
    name VARCHAR(30)
    FOREIGN KEY (id) REFERENCES movie_genres (genre_id)
);