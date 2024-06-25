# eliminamos la base
DROP DATABASE IF EXISTS Borbocoders;

# creamos la base de datos, con charset UTF8 para que tome correctamente los ascentos
CREATE DATABASE IF NOT EXISTS Borbocoders CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

# usamos la base de datos creada
USE Borbocoders;

# creamos a tabla productos
CREATE TABLE productos (
    id TINYINT(255) AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    precio INT(255) NOT NULL,
    imagen VARCHAR(255) NOT NULL
);


# estos son los productos del JS que tiene los productos
# solamente faltaría ajustar el tema de las rutas de las imágenes una vez que las subamos a algún hosting gratis
INSERT INTO productos (marca, nombre, precio, imagen)
VALUES
('Homen', 'Verum', '45000', 'img/1.jpg'),
('Biografia', 'Assinatura', '36000', 'img/2.jpg'),
('Essencial', 'Clasico', '55000', 'img/3.jpg'),
('Humor', 'Quimica de', '30000', 'img/4.jpg'),
('Kaiak', 'Ultra', '33000', 'img/5.jpg'),
('Kaiak', 'Exclusivo', '55000', 'img/6.jpg'),
('Luna', 'Absoluta', '39000', 'img/7.jpg'),
('Kriska', 'Drama', '26000', 'img/8.jpg'),
('Kriska', 'Alegria', '26000', 'img/9.jpg'),
('Luna', 'Intenso', '42000', 'img/10.jpg'),
('Ekos', 'Alma', '42000', 'img/11.jpg'),
('Essencial', 'Supreme', '39000', 'img/12.jpg')
;