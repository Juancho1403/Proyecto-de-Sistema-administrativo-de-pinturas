-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-12-2024 a las 01:57:36
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
-- Base de datos: `sistemas_de_programas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `id` int(11) NOT NULL,
  `producto` varchar(100) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `codigo` varchar(50) NOT NULL,
  `precio_base` varchar(100) NOT NULL,
  `impuesto` varchar(100) NOT NULL,
  `precio_total` varchar(100) NOT NULL,
  `fecha` varchar(100) NOT NULL,
  `detalles` text DEFAULT NULL,
  `solicitante` varchar(100) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `compras`
--

INSERT INTO `compras` (`id`, `producto`, `cantidad`, `codigo`, `precio_base`, `impuesto`, `precio_total`, `fecha`, `detalles`, `solicitante`) VALUES
(1, 'Producto A', 10, 'COD001', '90.00', '10.00', '100.00', '2024-11-17', 'Detalle A', 'Juan Pérez'),
(2, 'Producto B', 5, 'COD002', '120.00', '12.00', '132.00', '2024-11-17', 'Detalle B', 'María López'),
(3, 'Producto C', 20, 'COD003', '50.00', '5.00', '55.00', '2024-11-16', 'Detalle C', 'Carlos Gómez'),
(4, 'Producto D', 8, 'COD004', '200.00', '20.00', '220.00', '2024-11-15', 'Detalle D', 'Ana Torres'),
(5, 'Producto E', 15, 'COD005', '75.00', '7.50', '82.50', '2024-11-14', 'Detalle E', 'Luis Martínez'),
(6, 'Producto F', 12, 'COD006', '110.00', '11.00', '121.00', '2024-11-13', 'Detalle F', 'Sara Díaz'),
(7, 'Producto G', 25, 'COD007', '40.00', '4.00', '44.00', '2024-11-12', 'Detalle G', 'Pedro Ramírez'),
(8, 'Producto H', 18, 'COD008', '85.00', '8.50', '93.50', '2024-11-11', 'Detalle H', 'Julia Pérez'),
(9, 'Producto I', 10, 'COD009', '95.00', '9.50', '104.50', '2024-11-10', 'Detalle I', 'David Ortega'),
(10, 'Producto J', 30, 'COD010', '60.00', '6.00', '66.00', '2024-11-09', 'Detalle J', 'Elena García'),
(12, 'hojas', 25, '0001', '10', '15', '12', '2024-12-01', 'Pendiente', 'Juan Ruiz');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_compras`
--

CREATE TABLE `detalles_compras` (
  `detalles_compra_id` int(11) NOT NULL,
  `producto` text NOT NULL,
  `cantidad` int(11) NOT NULL,
  `id_compra` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalles_ventas`
--

CREATE TABLE `detalles_ventas` (
  `id_detalle` int(11) NOT NULL,
  `id_venta` int(11) NOT NULL,
  `id_producto` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `id` int(11) NOT NULL,
  `producto_nombre` text NOT NULL,
  `cantidad` int(11) NOT NULL,
  `producto_precio_base` float NOT NULL,
  `producto_impuesto` float NOT NULL,
  `producto_precio_total` float NOT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`id`, `producto_nombre`, `cantidad`, `producto_precio_base`, `producto_impuesto`, `producto_precio_total`, `id_usuario`) VALUES
(5, 'pintura blanca', 5, 10, 15, 12, 1),
(6, 'Pintura Clase A, Color Verde, Presentación 5 galones', 30, 120, 15, 138, 1),
(7, 'Pintura Clase B, Color Blanco, Presentación 1 galón', 60, 20, 15, 23, 1),
(8, 'Pintura Clase B, Color Blanco, Presentación 1/2 galón', 50, 12, 15, 13.8, 1),
(9, 'Pintura Clase B, Color Rojo, Presentación 1 galón', 45, 20, 15, 23, 1),
(10, 'Pintura Clase B, Color Rojo, Presentación 1/2 galón', 55, 12, 15, 13.8, 1),
(11, 'Pintura Clase B, Color Azul, Presentación 1 galón', 40, 20, 15, 23, 1),
(12, 'Pintura Clase B, Color Azul, Presentación 1/2 galón', 60, 12, 15, 13.8, 1),
(13, 'Pintura Clase B, Color Verde, Presentación 1 galón', 50, 20, 15, 23, 1),
(14, 'Pintura Clase B, Color Verde, Presentación 1/2 galón', 45, 12, 15, 13.8, 1),
(15, 'Pintura Clase C, Color Blanco, Presentación 1 galón', 70, 18, 15, 20.7, 1),
(16, 'Pintura Clase C, Color Blanco, Presentación 1/2 galón', 65, 10, 15, 11.5, 1),
(17, 'Pintura Clase C, Color Rojo, Presentación 1 galón', 55, 18, 15, 20.7, 1),
(18, 'Pintura Clase C, Color Rojo, Presentación 1/2 galón', 60, 10, 15, 11.5, 1),
(19, 'Pintura Clase C, Color Azul, Presentación 1 galón', 50, 18, 15, 20.7, 1),
(20, 'Pintura Clase C, Color Azul, Presentación 1/2 galón', 55, 10, 15, 11.5, 1),
(21, 'Pintura Clase C, Color Verde, Presentación 1 galón', 65, 18, 15, 20.7, 1),
(22, 'Pintura Clase C, Color Verde, Presentación 1/2 galón', 70, 10, 15, 11.5, 1),
(23, 'Brochas para Pintura, Tamaño Pequeño', 150, 2.5, 10, 2.75, 1),
(24, 'Brochas para Pintura, Tamaño Medio', 120, 3, 10, 3.3, 1),
(25, 'Brochas para Pintura, Tamaño Grande', 80, 3.5, 10, 3.85, 1),
(26, 'Rodillo para Pintura, Tamaño Pequeño', 90, 5.5, 10, 6.05, 1),
(27, 'Rodillo para Pintura, Tamaño Medio', 70, 6.5, 10, 7.15, 1),
(28, 'Rodillo para Pintura, Tamaño Grande', 60, 7.5, 10, 8.25, 1),
(29, 'Cinta de Enmascarar para Pintura, Ancho 1 pulgada', 160, 1.5, 10, 1.65, 1),
(30, 'Cinta de Enmascarar para Pintura, Ancho 2 pulgadas', 140, 2, 10, 2.2, 1),
(31, 'Lija Grano Fino para Madera', 200, 1, 10, 1.1, 1),
(32, 'Lija Grano Medio para Metal', 180, 1.2, 10, 1.32, 1),
(33, 'Masilla para Reparación de Paredes', 150, 3, 10, 3.3, 1),
(34, 'Masilla para Reparación de Pisos', 130, 3.5, 10, 3.85, 1),
(35, 'Barniz para Madera', 110, 5, 10, 5.5, 1),
(36, 'Barniz para Metal', 100, 5.5, 10, 6.05, 1),
(37, 'Disolvente para Pinturas', 90, 6, 10, 6.6, 1),
(38, 'Disolvente para Barnices', 80, 6.5, 10, 7.15, 1),
(39, 'Pintura Anticorrosiva, Color Gris, Presentación 1 galón', 75, 35, 15, 40.25, 1),
(40, 'Pintura Anticorrosiva, Color Gris, Presentación 5 galones', 50, 150, 15, 172.5, 1),
(41, 'Pintura Anticorrosiva, Color Negro, Presentación 1 galón', 60, 35, 15, 40.25, 1),
(42, 'Pintura Anticorrosiva, Color Negro, Presentación 5 galones', 55, 150, 15, 172.5, 1),
(43, 'Pintura Epóxica, Color Blanco, Presentación 1 galón', 45, 40, 15, 46, 1),
(44, 'Pintura Epóxica, Color Blanco, Presentación 5 galones', 35, 175, 15, 201.25, 1),
(45, 'Pintura Epóxica, Color Rojo, Presentación 1 galón', 40, 40, 15, 46, 1),
(46, 'Pintura Epóxica, Color Rojo, Presentación 5 galones', 30, 175, 15, 201.25, 1),
(47, 'Pintura Epóxica, Color Verde, Presentación 1 galón', 50, 40, 15, 46, 1),
(48, 'Pintura Epóxica, Color Verde, Presentación 5 galones', 40, 175, 15, 201.25, 1),
(49, 'Pintura Clásica, Color Blanco, Presentación 1 galón', 65, 15, 15, 17.25, 1),
(50, 'Pintura Clásica, Color Blanco, Presentación 5 galones', 45, 70, 15, 80.5, 1),
(51, 'Pintura Clásica, Color Rojo, Presentación 1 galón', 60, 15, 15, 17.25, 1),
(52, 'Pintura Clásica, Color Rojo, Presentación 5 galones', 40, 70, 15, 80.5, 1),
(53, 'Pintura Clásica, Color Azul, Presentación 1 galón', 55, 15, 15, 17.25, 1),
(54, 'Pintura Clásica, Color Azul, Presentación 5 galones', 60, 70, 15, 80.5, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_de_acciones`
--

CREATE TABLE `registro_de_acciones` (
  `id` int(11) NOT NULL,
  `usuario` int(11) NOT NULL,
  `fecha_de_cambio` datetime NOT NULL,
  `cambio_hecho` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `contrasena`, `email`, `telefono`) VALUES
(1, 'prueba', 'prueba', 'prueba@gmail.com', '04144092171'),
(2, 'prueba', 'prueba', 'prueba@gmail.com', '04144092171'),
(3, 'admin', 'admin', 'admin@gmail.com', '04144092171'),
(4, 'ADMIN', 'ADMIN', 'ADMIN1@GMAIL.COM', '04144092171');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `id_venta` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cliente` varchar(255) NOT NULL,
  `producto` varchar(255) NOT NULL,
  `monto_base` float NOT NULL,
  `monto_impuesto` float NOT NULL,
  `monto_total` float NOT NULL,
  `forma_pago` text NOT NULL,
  `igtf` float NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `observaciones` text DEFAULT NULL,
  `porcentaje` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`id_venta`, `fecha`, `cliente`, `producto`, `monto_base`, `monto_impuesto`, `monto_total`, `forma_pago`, `igtf`, `usuario_id`, `observaciones`, `porcentaje`) VALUES
(0, '2024-12-03', 'juan', '10', 15, 12, 0, '1', 0, 0, '16', 0),
(1, '2024-11-01', 'Cliente A', 'Pintura Acrílica', 100, 16, 116, 'Efectivo', 0, 1, 'Sin observaciones', 16),
(2, '2024-11-02', 'Cliente B', 'Pintura Base', 200, 32, 232, 'Transferencia', 1, 2, 'Pago rápido', 16),
(3, '2024-11-03', 'Cliente C', 'Pintura Sintética', 300, 48, 348, 'Tarjeta de crédito', 2, 3, 'Cliente frecuente', 16),
(4, '2024-11-04', 'Cliente D', 'Pintura para Madera', 400, 64, 464, 'Efectivo', 0, 4, 'Sin observaciones', 16),
(5, '2024-11-05', 'Cliente E', 'Imprimante Base', 150, 24, 174, 'Zelle', 1.5, 1, 'Observaciones: descuento aplicado', 16),
(6, '2024-11-06', 'Cliente F', 'Pintura Epóxica', 250, 40, 290, 'Pago móvil', 0.5, 5, 'Pago parcial', 16),
(7, '2024-11-07', 'Cliente G', 'Pintura para Exterior', 350, 56, 406, 'Tarjeta de débito', 0, 2, 'Cliente nuevo', 16),
(8, '2024-11-08', 'Cliente H', 'Pintura Texturizada', 450, 72, 522, 'Transferencia', 1.5, 3, 'Pago diferido', 16),
(9, '2024-11-09', 'Cliente I', 'Pintura para Interiores', 180, 28.8, 208.8, 'Efectivo', 0, 4, 'Sin observaciones', 16),
(10, '2024-11-10', 'juan Ruiz', 'Imprimante Especial', 10, 15, 12, 'Pago', 2, 5, 'Pago aprobado', 16);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `detalles_compras`
--
ALTER TABLE `detalles_compras`
  ADD PRIMARY KEY (`detalles_compra_id`);

--
-- Indices de la tabla `detalles_ventas`
--
ALTER TABLE `detalles_ventas`
  ADD PRIMARY KEY (`id_detalle`);

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_usuario` (`id_usuario`);

--
-- Indices de la tabla `registro_de_acciones`
--
ALTER TABLE `registro_de_acciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`id_venta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `detalles_compras`
--
ALTER TABLE `detalles_compras`
  MODIFY `detalles_compra_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalles_ventas`
--
ALTER TABLE `detalles_ventas`
  MODIFY `id_detalle` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT de la tabla `registro_de_acciones`
--
ALTER TABLE `registro_de_acciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
