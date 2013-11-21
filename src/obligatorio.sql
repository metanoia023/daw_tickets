-- phpMyAdmin SQL Dump
-- version 2.10.2
-- http://www.phpmyadmin.net
-- 
-- Servidor: localhost
-- Tiempo de generación: 21-11-2013 a las 17:11:19
-- Versión del servidor: 5.0.45
-- Versión de PHP: 5.2.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

-- 
-- Base de datos: `obligatorio`
-- 

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `auth_group`
-- 

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `auth_group`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `auth_group_permissions`
-- 

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `auth_group_permissions`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `auth_permission`
-- 

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=43 ;

-- 
-- Volcar la base de datos para la tabla `auth_permission`
-- 

INSERT INTO `auth_permission` VALUES (1, 'Can add permission', 1, 'add_permission');
INSERT INTO `auth_permission` VALUES (2, 'Can change permission', 1, 'change_permission');
INSERT INTO `auth_permission` VALUES (3, 'Can delete permission', 1, 'delete_permission');
INSERT INTO `auth_permission` VALUES (4, 'Can add group', 2, 'add_group');
INSERT INTO `auth_permission` VALUES (5, 'Can change group', 2, 'change_group');
INSERT INTO `auth_permission` VALUES (6, 'Can delete group', 2, 'delete_group');
INSERT INTO `auth_permission` VALUES (7, 'Can add user', 3, 'add_user');
INSERT INTO `auth_permission` VALUES (8, 'Can change user', 3, 'change_user');
INSERT INTO `auth_permission` VALUES (9, 'Can delete user', 3, 'delete_user');
INSERT INTO `auth_permission` VALUES (10, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (11, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (12, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (13, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (14, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (15, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (16, 'Can add site', 6, 'add_site');
INSERT INTO `auth_permission` VALUES (17, 'Can change site', 6, 'change_site');
INSERT INTO `auth_permission` VALUES (18, 'Can delete site', 6, 'delete_site');
INSERT INTO `auth_permission` VALUES (19, 'Can add categoria', 7, 'add_categoria');
INSERT INTO `auth_permission` VALUES (20, 'Can change categoria', 7, 'change_categoria');
INSERT INTO `auth_permission` VALUES (21, 'Can delete categoria', 7, 'delete_categoria');
INSERT INTO `auth_permission` VALUES (22, 'Can add espectaculo', 8, 'add_espectaculo');
INSERT INTO `auth_permission` VALUES (23, 'Can change espectaculo', 8, 'change_espectaculo');
INSERT INTO `auth_permission` VALUES (24, 'Can delete espectaculo', 8, 'delete_espectaculo');
INSERT INTO `auth_permission` VALUES (25, 'Can add precio', 9, 'add_precio');
INSERT INTO `auth_permission` VALUES (26, 'Can change precio', 9, 'change_precio');
INSERT INTO `auth_permission` VALUES (27, 'Can delete precio', 9, 'delete_precio');
INSERT INTO `auth_permission` VALUES (28, 'Can add lugar', 10, 'add_lugar');
INSERT INTO `auth_permission` VALUES (29, 'Can change lugar', 10, 'change_lugar');
INSERT INTO `auth_permission` VALUES (30, 'Can delete lugar', 10, 'delete_lugar');
INSERT INTO `auth_permission` VALUES (31, 'Can add sector', 11, 'add_sector');
INSERT INTO `auth_permission` VALUES (32, 'Can change sector', 11, 'change_sector');
INSERT INTO `auth_permission` VALUES (33, 'Can delete sector', 11, 'delete_sector');
INSERT INTO `auth_permission` VALUES (34, 'Can add ticket', 12, 'add_ticket');
INSERT INTO `auth_permission` VALUES (35, 'Can change ticket', 12, 'change_ticket');
INSERT INTO `auth_permission` VALUES (36, 'Can delete ticket', 12, 'delete_ticket');
INSERT INTO `auth_permission` VALUES (37, 'Can add usuario', 13, 'add_usuario');
INSERT INTO `auth_permission` VALUES (38, 'Can change usuario', 13, 'change_usuario');
INSERT INTO `auth_permission` VALUES (39, 'Can delete usuario', 13, 'delete_usuario');
INSERT INTO `auth_permission` VALUES (40, 'Can add pin', 14, 'add_pin');
INSERT INTO `auth_permission` VALUES (41, 'Can change pin', 14, 'change_pin');
INSERT INTO `auth_permission` VALUES (42, 'Can delete pin', 14, 'delete_pin');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `auth_user`
-- 

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL auto_increment,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

-- 
-- Volcar la base de datos para la tabla `auth_user`
-- 

INSERT INTO `auth_user` VALUES (1, 'admin', '', '', 'admin@admin.com', 'pbkdf2_sha256$10000$mwZP7NuMI72q$FZvnWtOerlTHjtMTVfkz3pAENKy5TeMhsvpKMLugGR0=', 1, 1, 1, '2013-11-21 17:08:46', '2013-11-21 17:08:46');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `auth_user_groups`
-- 

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `auth_user_groups`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `auth_user_user_permissions`
-- 

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL auto_increment,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- 
-- Volcar la base de datos para la tabla `auth_user_user_permissions`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `django_content_type`
-- 

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=15 ;

-- 
-- Volcar la base de datos para la tabla `django_content_type`
-- 

INSERT INTO `django_content_type` VALUES (1, 'permission', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (2, 'group', 'auth', 'group');
INSERT INTO `django_content_type` VALUES (3, 'user', 'auth', 'user');
INSERT INTO `django_content_type` VALUES (4, 'content type', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (5, 'session', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (6, 'site', 'sites', 'site');
INSERT INTO `django_content_type` VALUES (7, 'categoria', 'tickets', 'categoria');
INSERT INTO `django_content_type` VALUES (8, 'espectaculo', 'tickets', 'espectaculo');
INSERT INTO `django_content_type` VALUES (9, 'precio', 'tickets', 'precio');
INSERT INTO `django_content_type` VALUES (10, 'lugar', 'tickets', 'lugar');
INSERT INTO `django_content_type` VALUES (11, 'sector', 'tickets', 'sector');
INSERT INTO `django_content_type` VALUES (12, 'ticket', 'tickets', 'ticket');
INSERT INTO `django_content_type` VALUES (13, 'usuario', 'tickets', 'usuario');
INSERT INTO `django_content_type` VALUES (14, 'pin', 'tickets', 'pin');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `django_session`
-- 

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY  (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- 
-- Volcar la base de datos para la tabla `django_session`
-- 


-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `django_site`
-- 

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL auto_increment,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

-- 
-- Volcar la base de datos para la tabla `django_site`
-- 

INSERT INTO `django_site` VALUES (1, 'example.com', 'example.com');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_categoria`
-- 

CREATE TABLE `tickets_categoria` (
  `id` int(11) NOT NULL auto_increment,
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

-- 
-- Volcar la base de datos para la tabla `tickets_categoria`
-- 

INSERT INTO `tickets_categoria` VALUES (1, 'Música', 'Son espectáculos musicales');
INSERT INTO `tickets_categoria` VALUES (2, 'Teatro', 'Son piezas teatrales');
INSERT INTO `tickets_categoria` VALUES (3, 'Danza', 'Son shows de distintos tipos de danza');
INSERT INTO `tickets_categoria` VALUES (4, 'Stand Up', 'Comediantes de pie hacen chistes');
INSERT INTO `tickets_categoria` VALUES (5, 'Otros', 'Espectáculos varios');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_espectaculo`
-- 

CREATE TABLE `tickets_espectaculo` (
  `id` int(11) NOT NULL auto_increment,
  `nombre` varchar(20) NOT NULL,
  `lugar_id` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  `hora` datetime NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `descripcion` varchar(300) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `tickets_espectaculo_559e0e98` (`lugar_id`),
  KEY `tickets_espectaculo_64c3c188` (`categoria_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- 
-- Volcar la base de datos para la tabla `tickets_espectaculo`
-- 

INSERT INTO `tickets_espectaculo` VALUES (1, 'Laura Pausini', 1, 1, '2014-02-08 20:00:00', 0, 'El mejor espectáculo del año no te lo podés perder');
INSERT INTO `tickets_espectaculo` VALUES (2, 'Marc Anthony', 2, 1, '2014-01-24 21:00:00', 0, 'Marc Antony el mejor cantante latino de baladas romanticas');
INSERT INTO `tickets_espectaculo` VALUES (3, 'Maria Callas', 3, 1, '2013-10-01 19:00:00', 0, 'La diva numero uno de la opera contemporanea');
INSERT INTO `tickets_espectaculo` VALUES (4, 'Disney en Hielo', 3, 5, '2014-04-01 17:00:00', 0, 'Llega Disney sobre Hielo para delicia de chicos y grandes.');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_lugar`
-- 

CREATE TABLE `tickets_lugar` (
  `id` int(11) NOT NULL auto_increment,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- 
-- Volcar la base de datos para la tabla `tickets_lugar`
-- 

INSERT INTO `tickets_lugar` VALUES (1, 'Teatro de Verano');
INSERT INTO `tickets_lugar` VALUES (2, 'Sala Zitarrosa');
INSERT INTO `tickets_lugar` VALUES (3, 'Teatro Metro');
INSERT INTO `tickets_lugar` VALUES (4, 'Cine Plaza');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_pin`
-- 

CREATE TABLE `tickets_pin` (
  `numero` int(11) NOT NULL,
  `telefono_id` varchar(9) NOT NULL,
  PRIMARY KEY  (`telefono_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- 
-- Volcar la base de datos para la tabla `tickets_pin`
-- 

INSERT INTO `tickets_pin` VALUES (8489, '099421030');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_precio`
-- 

CREATE TABLE `tickets_precio` (
  `id` int(11) NOT NULL auto_increment,
  `precio` decimal(6,2) NOT NULL,
  `sector_id` int(11) NOT NULL,
  `espectaculo_id` int(11) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `tickets_precio_94c48b8` (`sector_id`),
  KEY `tickets_precio_1f728237` (`espectaculo_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=13 ;

-- 
-- Volcar la base de datos para la tabla `tickets_precio`
-- 

INSERT INTO `tickets_precio` VALUES (1, 3000.00, 25, 1);
INSERT INTO `tickets_precio` VALUES (2, 2500.00, 26, 1);
INSERT INTO `tickets_precio` VALUES (3, 1000.00, 27, 1);
INSERT INTO `tickets_precio` VALUES (4, 600.00, 28, 1);
INSERT INTO `tickets_precio` VALUES (5, 5000.00, 29, 2);
INSERT INTO `tickets_precio` VALUES (6, 4000.00, 30, 2);
INSERT INTO `tickets_precio` VALUES (7, 1500.00, 31, 2);
INSERT INTO `tickets_precio` VALUES (8, 800.00, 32, 2);
INSERT INTO `tickets_precio` VALUES (9, 4000.00, 33, 3);
INSERT INTO `tickets_precio` VALUES (10, 3000.00, 34, 3);
INSERT INTO `tickets_precio` VALUES (11, 1200.00, 35, 3);
INSERT INTO `tickets_precio` VALUES (12, 600.00, 36, 3);

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_sector`
-- 

CREATE TABLE `tickets_sector` (
  `id` int(11) NOT NULL auto_increment,
  `lugar_id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `asientos` int(11) NOT NULL,
  `ocupado` tinyint(1) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `tickets_sector_559e0e98` (`lugar_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=41 ;

-- 
-- Volcar la base de datos para la tabla `tickets_sector`
-- 

INSERT INTO `tickets_sector` VALUES (25, 1, 'Platea Vip', 100, 0);
INSERT INTO `tickets_sector` VALUES (26, 1, 'Platea Central', 200, 0);
INSERT INTO `tickets_sector` VALUES (27, 1, 'Super Pullman', 300, 0);
INSERT INTO `tickets_sector` VALUES (28, 1, 'Pullman', 1000, 0);
INSERT INTO `tickets_sector` VALUES (29, 2, 'Platea Vip', 100, 0);
INSERT INTO `tickets_sector` VALUES (30, 2, 'Platea Central', 1, 0);
INSERT INTO `tickets_sector` VALUES (31, 2, 'Super Pullman', 300, 0);
INSERT INTO `tickets_sector` VALUES (32, 2, 'Pullman', 500, 0);
INSERT INTO `tickets_sector` VALUES (33, 3, 'Platea Vip', 200, 0);
INSERT INTO `tickets_sector` VALUES (34, 3, 'Platea Central', 400, 0);
INSERT INTO `tickets_sector` VALUES (35, 3, 'Super Pullman', 600, 0);
INSERT INTO `tickets_sector` VALUES (36, 3, 'Pullman', 1000, 0);
INSERT INTO `tickets_sector` VALUES (37, 4, 'Platea Vip', 400, 0);
INSERT INTO `tickets_sector` VALUES (38, 4, 'Platea Central', 1500, 0);
INSERT INTO `tickets_sector` VALUES (39, 4, 'Super Pullman', 3000, 0);
INSERT INTO `tickets_sector` VALUES (40, 4, 'Pullman', 4000, 0);

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_ticket`
-- 

CREATE TABLE `tickets_ticket` (
  `id` int(11) NOT NULL auto_increment,
  `sector_id` int(11) NOT NULL,
  `espectaculo_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `precio` decimal(6,2) NOT NULL,
  `usuario_id` varchar(9) NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `tickets_ticket_94c48b8` (`sector_id`),
  KEY `tickets_ticket_1f728237` (`espectaculo_id`),
  KEY `tickets_ticket_363db8b9` (`usuario_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- 
-- Volcar la base de datos para la tabla `tickets_ticket`
-- 

INSERT INTO `tickets_ticket` VALUES (1, 25, 1, '2013-11-18 16:27:49', 3000.00, '99177848');
INSERT INTO `tickets_ticket` VALUES (2, 25, 1, '2013-11-18 16:39:25', 3000.00, '99404325');
INSERT INTO `tickets_ticket` VALUES (3, 30, 2, '2013-11-18 16:39:41', 1000.00, '99404325');
INSERT INTO `tickets_ticket` VALUES (4, 25, 1, '2013-11-18 16:40:17', 3000.00, '94109288');

-- --------------------------------------------------------

-- 
-- Estructura de tabla para la tabla `tickets_usuario`
-- 

CREATE TABLE `tickets_usuario` (
  `nombre` varchar(30) NOT NULL,
  `telefono` varchar(9) NOT NULL,
  `documento` varchar(11) NOT NULL,
  PRIMARY KEY  (`telefono`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- 
-- Volcar la base de datos para la tabla `tickets_usuario`
-- 

INSERT INTO `tickets_usuario` VALUES ('Lucia Araujo', '099177848', '31995210');
INSERT INTO `tickets_usuario` VALUES ('Maria Ronchi', '099404325', '39876051');
INSERT INTO `tickets_usuario` VALUES ('Juan Garcia', '099421030', '10239916');
INSERT INTO `tickets_usuario` VALUES ('Fernando Rosa', '094109288', '24406465');
