CREATE DATABASE mysitedb;
USE mysitedb;

CREATE TABLE tPeliculas (
id INTEGER PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(50), 
url_imagen VARCHAR (200), 
valoracion INTEGER, 
genero VARCHAR(50));

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
FOREIGN KEY(usuario_id) REFERENCES tUsuarios(id),
FOREIGN KEY(pelicula_id) REFERENCES tPeliculas(id));

INSERT INTO tPeliculas VALUES (1, "Buscando a Nemo", "https://es.web.img3.acsta.net/r_1920_1080/medias/nmedia/18/82/42/43/20076350.jpg", 3, "Infantil, Animación");
INSERT INTO tPeliculas VALUES (2, "Los Minions 2", "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/minions-2-poster-1580755834.jpg", 4, "Infantil, Animación");
INSERT INTO tPeliculas VALUES (3, "Kung Fu Panda", "https://m.media-amazon.com/images/I/51xlf28jbiL._SX260_.jpg", 5, "Infantil, Animación, Acción y aventuras");
INSERT INTO tPeliculas VALUES (4, "Interstellar", "https://4.bp.blogspot.com/-6r1mJPRbuz4/XNg0dLNqe3I/AAAAAAAACJE/OCcqoUy1FMYYyVJUN-daa85oLM84S-frwCLcBGAs/s1600/interestellar.jpg", 5, "Ciencia ficcion, Drama, Aventuras");
INSERT INTO tPeliculas VALUES (5, "El rey León", "https://m.media-amazon.com/images/I/81v-F+xMzmL.jpg", 3, "Infantil, Animación");

INSERT INTO tUsuarios VALUES (1, "Cristina", "Moreno", "cmorenob@gmail.com", "1234");
INSERT INTO tUsuarios VALUES (2, "Cristian", "Sánchez Bardo", "csanchezb@gmail.com", "1234");
INSERT INTO tUsuarios VALUES (3, "Laura", "García López", "lgarcial@gmail.com", "1234");
INSERT INTO tUsuarios VALUES (4, "Mario", "Pérez Hernández", "mperezh@gmail.com", "1234");
INSERT INTO tUsuarios VALUES (5, "Elena", "Molina Bermejo", "emolinab@gmail.com", "1234");

INSERT INTO tComentarios VALUES (1, "Fue mejor la primera", 2, 2);
INSERT INTO tComentarios VALUES (2, "Me encantó, la banda sonora fue genial", 1, 4);
INSERT INTO tComentarios VALUES (3, "Preciosa para ver con los niños", 3, 1);
INSERT INTO tComentarios VALUES (4, "Está muy sobrevalorada", 5, 3);
INSERT INTO tComentarios VALUES (5, "La mejor película de este siglo", 4, 5);
