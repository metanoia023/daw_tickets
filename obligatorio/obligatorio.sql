/*
SQLyog Ultimate v10.00 Beta1
MySQL - 5.5.27 : Database - obligatorio
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`obligatorio` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `obligatorio`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add categoria',7,'add_categoria'),(20,'Can change categoria',7,'change_categoria'),(21,'Can delete categoria',7,'delete_categoria'),(22,'Can add espectaculo',8,'add_espectaculo'),(23,'Can change espectaculo',8,'change_espectaculo'),(24,'Can delete espectaculo',8,'delete_espectaculo'),(25,'Can add precio',9,'add_precio'),(26,'Can change precio',9,'change_precio'),(27,'Can delete precio',9,'delete_precio'),(28,'Can add lugar',10,'add_lugar'),(29,'Can change lugar',10,'change_lugar'),(30,'Can delete lugar',10,'delete_lugar'),(31,'Can add sector',11,'add_sector'),(32,'Can change sector',11,'change_sector'),(33,'Can delete sector',11,'delete_sector'),(34,'Can add ticket',12,'add_ticket'),(35,'Can change ticket',12,'change_ticket'),(36,'Can delete ticket',12,'delete_ticket'),(37,'Can add usuario',13,'add_usuario'),(38,'Can change usuario',13,'change_usuario'),(39,'Can delete usuario',13,'delete_usuario'),(40,'Can add pin',14,'add_pin'),(41,'Can change pin',14,'change_pin'),(42,'Can delete pin',14,'delete_pin'),(43,'Can add telefono',15,'add_telefono'),(44,'Can change telefono',15,'change_telefono'),(45,'Can delete telefono',15,'delete_telefono');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`username`,`first_name`,`last_name`,`email`,`password`,`is_staff`,`is_active`,`is_superuser`,`last_login`,`date_joined`) values (1,'mery','','','metanoia023@gmail.com','pbkdf2_sha256$10000$8fAE9TJKKx9Q$Ox6ZgsY8Lv8zX9bI8N5/0Xrcv2ULsFwKQE8H1Pwq0Co=',1,1,1,'2013-11-10 02:38:39','2013-11-10 02:38:39');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`),
  CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`name`,`app_label`,`model`) values (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'categoria','tickets','categoria'),(8,'espectaculo','tickets','espectaculo'),(9,'precio','tickets','precio'),(10,'lugar','tickets','lugar'),(11,'sector','tickets','sector'),(12,'ticket','tickets','ticket'),(13,'usuario','tickets','usuario'),(14,'pin','tickets','pin'),(15,'telefono','tickets','telefono');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_3da3d3d8` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

/*Table structure for table `django_site` */

DROP TABLE IF EXISTS `django_site`;

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `django_site` */

insert  into `django_site`(`id`,`domain`,`name`) values (1,'example.com','example.com');

/*Table structure for table `tickets_categoria` */

DROP TABLE IF EXISTS `tickets_categoria`;

CREATE TABLE `tickets_categoria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tickets_categoria` */

insert  into `tickets_categoria`(`id`,`nombre`,`descripcion`) values (0,'',''),(1,'Musica','Son espectáculos musicales'),(2,'Teatro','Son piezas teatrales'),(3,'Danza','Son shows de distintos tipos de danza'),(4,'Stand Up','Comediantes de pie hacen chistes');

/*Table structure for table `tickets_espectaculo` */

DROP TABLE IF EXISTS `tickets_espectaculo`;

CREATE TABLE `tickets_espectaculo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `lugar_id` int(11) NOT NULL,
  `categoria_id` int(11) NOT NULL,
  `hora` datetime NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_espectaculo_559e0e98` (`lugar_id`),
  KEY `tickets_espectaculo_64c3c188` (`categoria_id`),
  CONSTRAINT `categoria_id_refs_id_29952fe` FOREIGN KEY (`categoria_id`) REFERENCES `tickets_categoria` (`id`),
  CONSTRAINT `lugar_id_refs_id_5b1164ea` FOREIGN KEY (`lugar_id`) REFERENCES `tickets_lugar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tickets_espectaculo` */

insert  into `tickets_espectaculo`(`id`,`nombre`,`lugar_id`,`categoria_id`,`hora`,`estado`,`descripcion`) values (1,'Laura Pausini',1,1,'2014-02-08 20:00:00',0,'El mejor espectaculo del anio no te lo podes perder'),(2,'Marc Anthony',2,1,'2014-01-24 21:00:00',0,'Marc Antony el mejor cantante latino de baladas romanticas'),(3,'Maria Callas',3,1,'2013-10-01 19:00:00',0,'La diva numero uno de la opera contemporanea');

/*Table structure for table `tickets_lugar` */

DROP TABLE IF EXISTS `tickets_lugar`;

CREATE TABLE `tickets_lugar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tickets_lugar` */

insert  into `tickets_lugar`(`id`,`nombre`) values (1,'Teatro de Verano'),(2,'Sala Zitarrosa'),(3,'Teatro Metro'),(4,'Cine Plaza');

/*Table structure for table `tickets_pin` */

DROP TABLE IF EXISTS `tickets_pin`;

CREATE TABLE `tickets_pin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(11) NOT NULL,
  `telefono_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_pin_1d373260` (`telefono_id`),
  CONSTRAINT `telefono_id_refs_id_34a9b490` FOREIGN KEY (`telefono_id`) REFERENCES `tickets_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tickets_pin` */

/*Table structure for table `tickets_precio` */

DROP TABLE IF EXISTS `tickets_precio`;

CREATE TABLE `tickets_precio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `precio` decimal(6,2) NOT NULL,
  `sector_id` int(11) NOT NULL,
  `espectaculo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_precio_94c48b8` (`sector_id`),
  KEY `tickets_precio_1f728237` (`espectaculo_id`),
  CONSTRAINT `espectaculo_id_refs_id_62bad950` FOREIGN KEY (`espectaculo_id`) REFERENCES `tickets_espectaculo` (`id`),
  CONSTRAINT `sector_id_refs_id_57c452d1` FOREIGN KEY (`sector_id`) REFERENCES `tickets_sector` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `tickets_precio` */

insert  into `tickets_precio`(`id`,`precio`,`sector_id`,`espectaculo_id`) values (1,'3000.00',25,1),(2,'2500.00',26,1),(3,'1000.00',27,1),(4,'600.00',28,1),(5,'5000.00',29,2),(6,'4000.00',30,2),(7,'1500.00',31,2),(8,'800.00',32,2),(9,'4000.00',33,3),(10,'3000.00',34,3),(11,'1200.00',35,3),(12,'600.00',36,3);

/*Table structure for table `tickets_sector` */

DROP TABLE IF EXISTS `tickets_sector`;

CREATE TABLE `tickets_sector` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lugar_id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `asientos` int(11) NOT NULL,
  `ocupado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_sector_559e0e98` (`lugar_id`),
  CONSTRAINT `lugar_id_refs_id_25436e51` FOREIGN KEY (`lugar_id`) REFERENCES `tickets_lugar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `tickets_sector` */

insert  into `tickets_sector`(`id`,`lugar_id`,`nombre`,`asientos`,`ocupado`) values (25,1,'Platea Vip',100,0),(26,1,'Platea Central',200,0),(27,1,'Super Pullman',300,0),(28,1,'Pullman',1000,0),(29,2,'Platea Vip',100,0),(30,2,'Platea Central',200,0),(31,2,'Super Pullman',300,0),(32,2,'Pullman',500,0),(33,3,'Platea Vip',200,0),(34,3,'Platea Central',400,0),(35,3,'Super Pullman',600,0),(36,3,'Pullman',1000,0),(37,4,'Platea Vip',400,0),(38,4,'Platea Central',1500,0),(39,4,'Super Pullman',3000,0),(40,4,'Pullman',4000,0);

/*Table structure for table `tickets_ticket` */

DROP TABLE IF EXISTS `tickets_ticket`;

CREATE TABLE `tickets_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lugar_id` int(11) NOT NULL,
  `espectaculo_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `precio` decimal(6,2) NOT NULL,
  `pin` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tickets_ticket_559e0e98` (`lugar_id`),
  KEY `tickets_ticket_1f728237` (`espectaculo_id`),
  KEY `tickets_ticket_363db8b9` (`usuario_id`),
  CONSTRAINT `espectaculo_id_refs_id_64eb178e` FOREIGN KEY (`espectaculo_id`) REFERENCES `tickets_espectaculo` (`id`),
  CONSTRAINT `lugar_id_refs_id_45eb2e17` FOREIGN KEY (`lugar_id`) REFERENCES `tickets_lugar` (`id`),
  CONSTRAINT `usuario_id_refs_id_6969d2a4` FOREIGN KEY (`usuario_id`) REFERENCES `tickets_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tickets_ticket` */

/*Table structure for table `tickets_usuario` */

DROP TABLE IF EXISTS `tickets_usuario`;

CREATE TABLE `tickets_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `telefono` varchar(9) NOT NULL,
  `documento` varchar(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tickets_usuario` */

insert  into `tickets_usuario`(`id`,`nombre`,`telefono`,`documento`) values (1,'Lucia Araujo','099177848','31995210'),(2,'Maria Ronchi','099404325','39876051'),(3,'Juan Garcia','099421030','10239916'),(4,'Fernando Rosa','094109288','24406465');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
