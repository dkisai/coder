CREATE TABLE Genres (
    id INT PRIMARY KEY,
    Nombre VARCHAR(30)
);

CREATE TABLE Countries (
    id INT PRIMARY KEY,
    iso_3166_1 VARCHAR(30),
    english_name VARCHAR(30),
    native_name VARCHAR(30)
);

CREATE TABLE Pelicula (
    id INT PRIMARY KEY,
    original_title VARCHAR(100),
    original_language VARCHAR(20),
    release_date DATE,
    title VARCHAR(100),
    tagline VARCHAR(100),
    runtime SMALLINT,
    poster_path VARCHAR(100),
    budget INT,
    revenue INT,
    genre INT,
    country INT,
    overview TEXT,
    FOREIGN KEY (genre) REFERENCES Genres(id),
    FOREIGN KEY (country) REFERENCES Countries(id)
);
