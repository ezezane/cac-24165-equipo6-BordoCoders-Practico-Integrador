-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-06-2024 a las 01:58:33
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `productos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `precio` float NOT NULL,
  `url img` varchar(75) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `marca`, `precio`, `url img`) VALUES
(1, 'Verum', 'Homen', 45000, 'img/1.jpg'),
(2, 'Assinatura', 'Biografia', 36000, 'img/2.jpg'),
(3, 'Clasico', 'Essencial', 55000, 'img/3.jpg'),
(4, 'Quimica de', 'Humor', 30000, 'img/4.jpg'),
(5, 'Ultra', 'Kaiak', 33000, 'img/5.jpg'),
(6, 'Exclusivo', 'Kaiak', 55000, 'img/6.jpg'),
(7, 'Absoluta', 'Luna', 39000, 'img/7.jpg'),
(8, 'Drama', 'Kriska', 26000, 'img/8.jpg'),
(9, 'Alegria', 'Kriska', 26000, 'img/9.jpg'),
(10, 'Intenso', 'Luna', 42000, 'img/10.jpg'),
(11, 'Alma', 'Ekos', 42000, 'img/11.jpg'),
(12, 'Supreme', 'Essencial', 39000, 'img/12.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
