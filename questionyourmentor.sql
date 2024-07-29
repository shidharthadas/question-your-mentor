-- Adminer 4.8.1 MySQL 5.7.36 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

CREATE DATABASE `questionyourmentor` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `questionyourmentor`;

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1,	'Can add log entry',	1,	'add_logentry'),
(2,	'Can change log entry',	1,	'change_logentry'),
(3,	'Can delete log entry',	1,	'delete_logentry'),
(4,	'Can view log entry',	1,	'view_logentry'),
(5,	'Can add permission',	2,	'add_permission'),
(6,	'Can change permission',	2,	'change_permission'),
(7,	'Can delete permission',	2,	'delete_permission'),
(8,	'Can view permission',	2,	'view_permission'),
(9,	'Can add group',	3,	'add_group'),
(10,	'Can change group',	3,	'change_group'),
(11,	'Can delete group',	3,	'delete_group'),
(12,	'Can view group',	3,	'view_group'),
(13,	'Can add content type',	4,	'add_contenttype'),
(14,	'Can change content type',	4,	'change_contenttype'),
(15,	'Can delete content type',	4,	'delete_contenttype'),
(16,	'Can view content type',	4,	'view_contenttype'),
(17,	'Can add session',	5,	'add_session'),
(18,	'Can change session',	5,	'change_session'),
(19,	'Can delete session',	5,	'delete_session'),
(20,	'Can view session',	5,	'view_session'),
(21,	'Can add user',	6,	'add_user'),
(22,	'Can change user',	6,	'change_user'),
(23,	'Can delete user',	6,	'delete_user'),
(24,	'Can view user',	6,	'view_user'),
(25,	'Can add query',	7,	'add_query'),
(26,	'Can change query',	7,	'change_query'),
(27,	'Can delete query',	7,	'delete_query'),
(28,	'Can view query',	7,	'view_query'),
(29,	'Can add log',	8,	'add_log'),
(30,	'Can change log',	8,	'change_log'),
(31,	'Can delete log',	8,	'delete_log'),
(32,	'Can view log',	8,	'view_log');

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_questionyourmentor_user_id` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1,	'admin',	'logentry'),
(3,	'auth',	'group'),
(2,	'auth',	'permission'),
(4,	'contenttypes',	'contenttype'),
(8,	'questionyourmentor',	'log'),
(7,	'questionyourmentor',	'query'),
(6,	'questionyourmentor',	'user'),
(5,	'sessions',	'session');

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1,	'contenttypes',	'0001_initial',	'2021-03-07 11:57:06.195508'),
(2,	'admin',	'0001_initial',	'2021-03-07 11:57:06.970794'),
(3,	'admin',	'0002_logentry_remove_auto_add',	'2021-03-07 11:57:10.544386'),
(4,	'admin',	'0003_logentry_add_action_flag_choices',	'2021-03-07 11:57:10.687109'),
(5,	'contenttypes',	'0002_remove_content_type_name',	'2021-03-07 11:57:13.147611'),
(6,	'auth',	'0001_initial',	'2021-03-07 11:57:15.211652'),
(7,	'auth',	'0002_alter_permission_name_max_length',	'2021-03-07 11:57:25.597788'),
(8,	'auth',	'0003_alter_user_email_max_length',	'2021-03-07 11:57:25.774061'),
(9,	'auth',	'0004_alter_user_username_opts',	'2021-03-07 11:57:25.982091'),
(10,	'auth',	'0005_alter_user_last_login_null',	'2021-03-07 11:57:26.132546'),
(11,	'auth',	'0006_require_contenttypes_0002',	'2021-03-07 11:57:26.372166'),
(12,	'auth',	'0007_alter_validators_add_error_messages',	'2021-03-07 11:57:26.521407'),
(13,	'auth',	'0008_alter_user_username_max_length',	'2021-03-07 11:57:26.743385'),
(14,	'auth',	'0009_alter_user_last_name_max_length',	'2021-03-07 11:57:26.866232'),
(15,	'auth',	'0010_alter_group_name_max_length',	'2021-03-07 11:57:27.454424'),
(16,	'auth',	'0011_update_proxy_permissions',	'2021-03-07 11:57:27.659476'),
(17,	'auth',	'0012_alter_user_first_name_max_length',	'2021-03-07 11:57:27.877278'),
(18,	'sessions',	'0001_initial',	'2021-03-07 11:57:28.835747');

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `questionyourmentor_log`;
CREATE TABLE `questionyourmentor_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `content_type` text COLLATE utf8_unicode_ci NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `questionyourmentor_log` (`id`, `action_time`, `content_type`, `user_id`) VALUES
(1,	'2021-03-14 06:59:55.170642',	'Viewed all query',	1),
(2,	'2021-03-14 07:03:17.584163',	'Viewed all query',	1),
(3,	'2021-03-14 07:03:23.067158',	'Viewed all query',	1),
(4,	'2021-03-14 07:03:28.531826',	'Viewed all query',	1),
(5,	'2021-03-14 07:21:45.100638',	'Viewed all query',	1),
(6,	'2021-03-15 07:56:31.419684',	'Viewed all query',	1),
(7,	'2021-03-15 08:09:33.627212',	'Viewed all query',	1);

DROP TABLE IF EXISTS `questionyourmentor_query`;
CREATE TABLE `questionyourmentor_query` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `mentor_user_id` int(11) NOT NULL,
  `query_message` text COLLATE utf8_unicode_ci NOT NULL,
  `attachment` text COLLATE utf8_unicode_ci,
  `query_time` datetime(6) NOT NULL,
  `response_message` text COLLATE utf8_unicode_ci,
  `response_time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `questionyourmentor_query` (`id`, `user_id`, `mentor_user_id`, `query_message`, `attachment`, `query_time`, `response_message`, `response_time`) VALUES
(6,	3,	1,	'abc def',	'',	'2021-03-13 18:36:21.622770',	'asd',	'2021-03-13 19:31:45.193234'),
(7,	3,	2,	'abc def',	'',	'2021-03-13 18:39:22.706773',	'',	'2021-03-13 18:39:22.706773'),
(8,	3,	2,	'abc def',	'user_3/1607498433088.jpg',	'2021-03-13 18:39:48.615828',	'',	'2021-03-13 18:39:48.615828'),
(9,	3,	2,	'abc def',	'user_3/1607498433088_uyRr1Jd.jpg',	'2021-03-13 19:34:19.801347',	'',	'2021-03-13 19:34:19.802370'),
(10,	3,	2,	'abc def',	'',	'2021-03-13 19:38:37.764829',	'',	'2021-03-13 19:38:37.765827'),
(11,	3,	2,	'abc def',	'user_3/1607498433088.jpg',	'2021-03-13 19:39:09.411455',	'',	'2021-03-13 19:39:09.411455'),
(12,	3,	2,	'abc def',	'user_3/1607498433088_gSaYpoB.jpg',	'2021-03-14 05:01:20.644412',	'',	'2021-03-14 05:01:20.644412'),
(13,	3,	2,	'abc def',	'user_3/1607498433088_ib5IvLN.jpg',	'2021-03-14 05:22:48.327327',	'',	'2021-03-14 05:22:48.327327');

DROP TABLE IF EXISTS `questionyourmentor_user`;
CREATE TABLE `questionyourmentor_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `role` varchar(7) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `first_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `questionyourmentor_user` (`id`, `password`, `last_login`, `is_superuser`, `role`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1,	'pbkdf2_sha256$216000$FPOoifutduf8$iIdaHXVp8scqpEkEzt5zKec27X76O1NP/8/Ynbo38kU=',	'2021-03-07 11:59:02.890538',	1,	'Mentor',	NULL,	'Shidhartha',	'Das',	'shidhadas2@gmail.com',	1,	1,	'2021-03-07 11:59:03.243532'),
(2,	'pbkdf2_sha256$216000$guJrLVG80Axw$ctp09XtN/7hZUuKP2pXicrNI5kjofIXu4qRQ2eQ61PY=',	'2021-03-07 12:00:43.334594',	1,	'Mentor',	NULL,	'Arijit',	'Sarkar',	'arijit@gmail.com',	1,	1,	'2021-03-07 12:00:43.679612'),
(3,	'pbkdf2_sha256$216000$RCf7OChNxhza$g1qI1oZ7WdKYs7aOPi3/5WaP8OHB5J+HH/M5HbKoO4Y=',	NULL,	0,	'User',	NULL,	'Arman',	'Hesmi',	'a@gmail.com',	0,	1,	'2021-03-07 13:05:55.207897'),
(4,	'pbkdf2_sha256$216000$misRlLkCuCCc$M8uZXZDrmps/ESNLNgCQ1rYbqGVpQMF1YyO+yqkPQ/I=',	NULL,	0,	'User',	NULL,	'asd',	'sdf',	'b@gmail.com',	0,	1,	'2021-03-07 14:06:13.636025'),
(5,	'pbkdf2_sha256$216000$xCXP5z54L3pI$N+iqAGly8/LQFJgeRq0ymwRoYD7ZxRoh8Kv48IdM9D8=',	NULL,	0,	'User',	NULL,	'Camelia',	'Eris',	'c@gmail.com',	0,	1,	'2021-03-08 03:28:03.326444'),
(6,	'pbkdf2_sha256$216000$bVadxTA4g9Oo$2vgofnCFjoaaLFepWz7ydXvthBKm/WzA0M/C1Div/0E=',	NULL,	0,	'User',	NULL,	'Daunte',	'Eris',	'd@gmail.com',	0,	1,	'2021-03-14 04:58:37.035879'),
(7,	'pbkdf2_sha256$216000$iGFAtero8KRp$LiNclCyx+A6cjO+YJOyrayP719uNqBSDxsUyT8OjU8g=',	NULL,	0,	'User',	NULL,	'Evelyn',	'Eris',	'e@gmail.com',	0,	1,	'2021-03-14 05:39:16.011490');

-- 2022-08-23 10:58:26
