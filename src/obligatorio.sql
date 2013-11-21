-- phpMyAdmin SQL Dump
-- version 2.10.2
-- http://www.phpmyadmin.net
-- 
-- Servidor: localhost
-- Tiempo de generación: 21-11-2013 a las 21:21:09
-- Versión del servidor: 5.0.45
-- Versión de PHP: 5.2.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- Base de datos: `obligatorio`
-- 

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_ticket`
-- 

CREATE TABLE `tickets_ticket` (
  `id` int(11) NOT NULL auto_increment,
  `sector_id` int(11) NOT NULL,
  `espectaculo_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `usuario_id` varchar(9) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `tickets_ticket_94c48b8` (`sector_id`),
  KEY `tickets_ticket_1f728237` (`espectaculo_id`),
  KEY `tickets_ticket_363db8b9` (`usuario_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=31 ;

-- 
-- Volcar la base de datos para la tabla `tickets_ticket`
-- 

INSERT INTO `tickets_ticket` VALUES (1, 25, 1, '2013-11-18 16:27:49', '99177848');
INSERT INTO `tickets_ticket` VALUES (2, 25, 1, '2013-11-18 16:39:25', '99404325');
INSERT INTO `tickets_ticket` VALUES (3, 30, 2, '2013-11-18 16:39:41', '99404325');
INSERT INTO `tickets_ticket` VALUES (4, 25, 1, '2013-11-18 16:40:17', '94109288');
INSERT INTO `tickets_ticket` VALUES (30, 28, 1, '2013-11-21 23:16:10', '096777333');
INSERT INTO `tickets_ticket` VALUES (29, 28, 1, '2013-11-21 23:16:10', '096777333');
INSERT INTO `tickets_ticket` VALUES (28, 28, 1, '2013-11-21 23:16:10', '096777333');
INSERT INTO `tickets_ticket` VALUES (27, 28, 1, '2013-11-21 23:16:10', '096777333');
