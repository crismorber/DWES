CREATE DATABASE msitedb;

CREATE TABLE tPeliculas (
id INTEGER PRIMARY KEY AUTO_INCREMENT, 
nombre VARCHAR(50), 
url_imagen (VARCHAR 200), 
director(es) VARCHAR(100), 
genero (VARCHAR 100));

CREATE TABLE tUsuarios (
id INTEGER PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(50),
apellidos VARCHAR(50),
email VARCHAR(200) unique,
contraseña VARCHAR(200));

CREATE TABLE tComentarios (
id INTEGER PRIMARY KEY AUTO_INCREMENT,
comentarios VARCHAR(2000),
usuario_id INTEGER,
pelicula_id INTEGER,
FOREIGN KEY (usuario_id) REFERENCES tUsuarios(id),
FOREIGN KEY (pelicula_id) REFERENCES tPeliculas(id));