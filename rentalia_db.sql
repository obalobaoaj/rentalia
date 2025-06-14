-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 14, 2025 at 09:11 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rentalia_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add vehicle', 7, 'add_vehicle'),
(26, 'Can change vehicle', 7, 'change_vehicle'),
(27, 'Can delete vehicle', 7, 'delete_vehicle'),
(28, 'Can view vehicle', 7, 'view_vehicle'),
(29, 'Can add rental', 8, 'add_rental'),
(30, 'Can change rental', 8, 'change_rental'),
(31, 'Can delete rental', 8, 'delete_rental'),
(32, 'Can view rental', 8, 'view_rental'),
(33, 'Can add location', 9, 'add_location'),
(34, 'Can change location', 9, 'change_location'),
(35, 'Can delete location', 9, 'delete_location'),
(36, 'Can view location', 9, 'view_location'),
(37, 'Can add earnings', 10, 'add_earnings'),
(38, 'Can change earnings', 10, 'change_earnings'),
(39, 'Can delete earnings', 10, 'delete_earnings'),
(40, 'Can view earnings', 10, 'view_earnings');

-- --------------------------------------------------------

--
-- Table structure for table `core_user`
--

CREATE TABLE `core_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_vehicle_owner` tinyint(1) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `age` int(10) UNSIGNED DEFAULT NULL CHECK (`age` >= 0),
  `date_of_birth` date DEFAULT NULL,
  `driver_license_picture` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `core_user`
--

INSERT INTO `core_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_vehicle_owner`, `phone_number`, `address`, `profile_picture`, `age`, `date_of_birth`, `driver_license_picture`) VALUES
(1, 'pbkdf2_sha256$600000$8sM12INmdeTUBYgyeNb689$+jtRSRLF1o705rxdP8llQiS8Z5PQ7D1hEkDdBF6frjk=', '2025-06-06 15:56:25.689459', 0, 'tellellycha', '', '', 'ajobalobao09@gmail.com', 0, 1, '2025-06-04 04:56:53.281696', 1, '09702268904', 'cagay', 'profile_pics/main_visual_2.png', NULL, NULL, ''),
(2, 'pbkdf2_sha256$600000$Q6geLYAqAKVDBFV05Jp2cm$O6n8CIRk8MNWvUvhH6viHZeweM0KokQPhojM4R4daSU=', '2025-06-14 07:07:42.346053', 1, 'rentalia', 'AJ', 'Obalobao', 'ajobalobao246@gmail.com', 1, 1, '2025-06-04 05:17:11.024087', 0, '', '', 'profile_pictures/Rentalia.png', NULL, NULL, ''),
(3, 'pbkdf2_sha256$600000$fyzHCYVDmdSx3AyzOE7Wfl$4rYfUObjSzkwHKma2Se9Fqp2LJzBW4JYwQCPiuyIv0s=', '2025-06-04 07:30:06.131391', 0, 'tellellycha1', '', '', 'ajobalobao09@gmail.com', 0, 1, '2025-06-04 07:29:58.582115', 1, '09702268904', 'cagay', '', NULL, NULL, ''),
(4, 'pbkdf2_sha256$600000$btoQkUFsnxWAEeg3YON7UO$V3NDKV/6dvz9H2r7xwYUBmfl44bCNonBSONvGygWdXc=', '2025-06-05 06:59:08.975353', 0, 'hopesfromnayeon', '', '', 'ajobalobao@filamer.edu.ph', 0, 1, '2025-06-05 06:59:08.706164', 1, '4523423423', 'cagay', 'profile_pictures/Chill_Guy.webp', NULL, NULL, ''),
(6, 'pbkdf2_sha256$600000$ROCmJp8YPA8is4yEJhq9nH$rGBtf4mWX3fUUzJ0+cWf3s2N17PsU/KRBbzi+Ri0hU8=', '2025-06-11 05:27:21.380866', 0, 'admin123', '', '', 'ajobalobao@filamer.edu.ph', 0, 1, '2025-06-05 08:20:30.007994', 0, '1241241241', 'Roxas city Capiz', 'profile_pictures/Chill_Guy_Bkqx1B1.webp', NULL, NULL, ''),
(8, 'pbkdf2_sha256$600000$3VJYms6yM5Us5z9L34tDBq$gdDHLeUWyzD8XKXg1ZS6NVn67yJlSc5Ng4cKflO+yAQ=', '2025-06-05 13:06:53.168988', 1, 'ajobalobao', '', '', 'ajobalobao@gmail.com', 1, 1, '2025-06-05 13:05:24.640247', 0, '', '', '', NULL, NULL, ''),
(9, 'pbkdf2_sha256$600000$lfIchMwKajbNd7jFs2GKEb$i/GxvoteCOjhYZA/xppxHtSzxbwB6iI5ko4zxt2jq/o=', '2025-06-06 09:03:34.223449', 0, 'cutelazycha', '', '', 'ajobalobao@example.com', 0, 1, '2025-06-06 09:03:33.852826', 0, '42343245235', 'rwetwetwertwer', 'profile_pictures/lance.jpg', NULL, NULL, ''),
(10, 'pbkdf2_sha256$600000$Civ20LIZJeXJYoeQ8qgBA9$abqKYl+jdxR2WfCxOuWnTK9cuzSEyM1FKLk4QsA34zQ=', '2025-06-06 09:25:49.949907', 0, 'hahaha123', 'ha', 'lee', 'ajobalobao@examplqe.com', 0, 1, '2025-06-06 09:25:49.716925', 0, '46545654645654', 'cagay roxas', 'profile_pictures/Chill_Guy_VELV4Vp.webp', NULL, NULL, ''),
(11, 'pbkdf2_sha256$600000$ABfHnvwnpAqmpoXydT3ACG$CTSc1eLcxQFIf6Tu6R1a2Dw8WklxGthV8P7hZvYFUsQ=', '2025-06-11 04:55:04.897306', 1, 'rentalia2', '', '', 'ajobalobao09@gmail.com', 1, 1, '2025-06-11 04:54:48.141472', 0, '', '', '', NULL, NULL, ''),
(12, 'pbkdf2_sha256$600000$Qtyt6ulvLvf4Ex5x3wgr9z$EHJXe+vaUpsLOWVW+QCCKESuWYDR/UaVIPUarM9Ka7M=', '2025-06-11 05:25:41.142354', 0, 'showmaker', 'show', 'maker', 'example@example.com', 0, 1, '2025-06-11 05:23:48.072186', 0, '124124123412', 'diri sa balay', 'profile_pictures/Mercedes_benz_glc.png', NULL, NULL, ''),
(13, 'pbkdf2_sha256$600000$9D7cYJPI0WV1LXjtFT2OOJ$OJy8cN1TnCI0peNa512LJPeqvAXHrKKIRg0k3EK10fQ=', '2025-06-12 04:25:01.255165', 0, 'cutelazycat1', 'cat', 'dog', 'dog@gmail.com', 0, 1, '2025-06-12 04:25:01.032796', 0, '', '', '', NULL, NULL, ''),
(14, 'pbkdf2_sha256$600000$CedFUYYfcRbMvfaMWAUeKc$I9dxQZUYbIYlyO352twdwWaHqD5icUzkUSNHUdM8Dbg=', '2025-06-14 07:07:11.130364', 0, 'catdog', 'rwqerwerw', 'wtrertertre', 'awrtwrw@gmai.com', 0, 1, '2025-06-12 04:26:30.513116', 0, '', '', '', NULL, NULL, ''),
(17, 'pbkdf2_sha256$600000$44lPuR4iegHyqaf6ISRPxN$6JbfNYcNfC0txl6t21IsXIrWpdsjjtim6QdGYFsoT84=', NULL, 1, 'admin', '', '', 'admin@example.com', 1, 1, '2025-06-12 04:49:48.397653', 0, '', '', '', NULL, NULL, ''),
(18, 'pbkdf2_sha256$600000$eoxkFJKNRtUd4joYY0pV7V$9kAsIvgD47eWptiHNNocZa+Az2o+ijB8md4ZirWVERQ=', '2025-06-12 08:02:41.827324', 0, 'john123', 'john', 'delecruz', 'ajobalobao@rwerwexample.com', 0, 1, '2025-06-12 08:02:41.594079', 0, '4213423432', 'cagay', 'profile_pictures/GLC.png', NULL, NULL, ''),
(19, 'pbkdf2_sha256$600000$TNDnWuGhXtQFBHhRdJSD2E$KeDhSmTdoIwfjDnRL23WITrsn3ey1LovQlmUp/46Lm8=', '2025-06-12 09:40:18.094599', 0, 'takeyourtime111', 'ar', 'ar', 'Ar@example.com', 0, 1, '2025-06-12 09:39:41.062526', 0, '09432534534534', 'cagay', 'profile_pictures/Raptor.png', NULL, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `core_user_groups`
--

CREATE TABLE `core_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_user_user_permissions`
--

CREATE TABLE `core_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-06-04 05:24:09.962407', '1', '2024 Hyundai Stargazer', 1, '[{\"added\": {}}]', 7, 2),
(2, '2025-06-04 05:53:02.782510', '2', '2025 Honda CR-V', 1, '[{\"added\": {}}]', 7, 2),
(3, '2025-06-04 06:01:33.727418', '3', '2023 Porsche 911 Carrera', 1, '[{\"added\": {}}]', 7, 2),
(4, '2025-06-04 06:02:20.660560', '3', '2023 Porsche 911 Carrera', 2, '[{\"changed\": {\"fields\": [\"Vehicle type\", \"Is available\"]}}]', 7, 2),
(5, '2025-06-04 07:10:20.839226', '1', 'Roxas,City', 1, '[{\"added\": {}}]', 9, 2),
(6, '2025-06-04 07:10:39.714723', '2', 'Ivisan,Capiz', 1, '[{\"added\": {}}]', 9, 2),
(7, '2025-06-04 07:11:02.979245', '3', 'President,Roxas', 1, '[{\"added\": {}}]', 9, 2),
(8, '2025-06-05 04:47:31.336095', '3', '2023 Porsche 911 Carrera', 2, '[{\"changed\": {\"fields\": [\"Vehicle type\", \"Location\"]}}]', 7, 2),
(9, '2025-06-05 04:47:44.451052', '2', '2025 Honda CR-V', 2, '[{\"changed\": {\"fields\": [\"Vehicle type\"]}}]', 7, 2),
(10, '2025-06-05 04:51:18.818326', '4', '2022 Hyundai Stargazer', 1, '[{\"added\": {}}]', 7, 2),
(11, '2025-06-05 04:52:50.637233', '1', '2024 Hyundai Stargazer', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 7, 2),
(12, '2025-06-05 04:56:45.859062', '2', '2025 Honda CR-V', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 7, 2),
(13, '2025-06-05 04:56:48.562782', '3', '2023 Porsche 911 Carrera', 2, '[]', 7, 2),
(14, '2025-06-05 06:34:11.371100', '5', '2023 Toyota Avanza', 1, '[{\"added\": {}}]', 7, 2),
(15, '2025-06-05 08:23:01.844704', '6', '2023 Porsche 911 Carrera', 1, '[{\"added\": {}}]', 7, 2),
(16, '2025-06-05 09:49:36.887683', '4', '2022 Hyundai Stargazer', 2, '[{\"changed\": {\"fields\": [\"Is available\"]}}]', 7, 2),
(17, '2025-06-06 08:48:13.688939', '1', 'Earnings for Rental #15 - 2022 Hyundai Stargazer', 2, '[{\"changed\": {\"fields\": [\"Payment status\", \"Paid at\"]}}]', 10, 2),
(18, '2025-06-06 09:17:39.718742', '7', '2021 Mercedes Benz GLC', 1, '[{\"added\": {}}]', 7, 2),
(19, '2025-06-06 15:53:57.916437', '3', 'Earnings for Rental #17 - 2023 Toyota Avanza', 2, '[{\"changed\": {\"fields\": [\"Payment status\", \"Paid at\"]}}]', 10, 2),
(20, '2025-06-10 03:28:31.836334', '4', 'Earnings for Rental #18 - 2021 Mercedes Benz GLC', 2, '[{\"changed\": {\"fields\": [\"Payment status\", \"Paid at\"]}}]', 10, 2),
(21, '2025-06-11 05:11:59.155079', '8', '2022 Nissan Patrol', 1, '[{\"added\": {}}]', 7, 2),
(22, '2025-06-11 05:14:54.442918', '4', 'Panitan', 1, '[{\"added\": {}}]', 9, 2),
(23, '2025-06-12 05:09:30.100389', '11', 'Roxas,City Capiz', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 2),
(24, '2025-06-12 05:10:01.461651', '10', 'Ivisan,Capiz', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 2),
(25, '2025-06-12 05:10:28.273629', '9', 'President,Roxas Capiz', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 9, 2),
(26, '2025-06-12 05:13:08.215369', '15', '2024 Hyundai Stargazer', 1, '[{\"added\": {}}]', 7, 2),
(27, '2025-06-12 05:35:44.062579', '14', '2023 Tesla Model 3', 2, '[{\"changed\": {\"fields\": [\"Daily rate\", \"Owner\"]}}]', 7, 2),
(28, '2025-06-12 05:36:13.708203', '8', 'Earnings for Rental #22 - 2023 Ford Raptor', 2, '[{\"changed\": {\"fields\": [\"Payment status\", \"Paid at\"]}}]', 10, 2),
(29, '2025-06-13 13:46:40.000121', '14', '2023 Tesla Model 3', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 2);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'core', 'user'),
(5, 'sessions', 'session'),
(10, 'vehicles', 'earnings'),
(9, 'vehicles', 'location'),
(8, 'vehicles', 'rental'),
(7, 'vehicles', 'vehicle');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-06-02 14:55:13.491142'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-06-02 14:55:13.535019'),
(3, 'auth', '0001_initial', '2025-06-02 14:55:13.700805'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-06-02 14:55:13.738228'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-06-02 14:55:13.742448'),
(6, 'auth', '0004_alter_user_username_opts', '2025-06-02 14:55:13.746525'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-06-02 14:55:13.750382'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-06-02 14:55:13.752340'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-06-02 14:55:13.756506'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-06-02 14:55:13.761045'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-06-02 14:55:13.765038'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-06-02 14:55:13.773278'),
(13, 'auth', '0011_update_proxy_permissions', '2025-06-02 14:55:13.777859'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-06-02 14:55:13.782029'),
(15, 'core', '0001_initial', '2025-06-02 14:55:13.965114'),
(16, 'admin', '0001_initial', '2025-06-02 14:55:14.049556'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-06-02 14:55:14.055019'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-06-02 14:55:14.060478'),
(19, 'sessions', '0001_initial', '2025-06-02 14:55:14.081444'),
(20, 'vehicles', '0001_initial', '2025-06-02 14:55:14.202236'),
(21, 'core', '0002_user_age_user_date_of_birth_and_more', '2025-06-04 03:10:10.999807'),
(22, 'vehicles', '0002_location_alter_vehicle_vehicle_type', '2025-06-04 06:38:03.718388'),
(23, 'vehicles', '0003_vehicle_location', '2025-06-04 07:08:52.549433'),
(24, 'core', '0003_alter_user_phone_number_alter_user_profile_picture', '2025-06-06 08:41:22.780129'),
(25, 'vehicles', '0004_rental_commission_rate_earnings', '2025-06-06 08:41:22.851019'),
(26, 'vehicles', '0005_vehicle_latitude_vehicle_location_address_and_more', '2025-06-12 04:15:50.399423'),
(27, 'vehicles', '0006_location_address_location_latitude_and_more', '2025-06-12 04:49:43.537530');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2at4lko67pdgses554v1ku37wsmre796', '.eJxVjMsOwiAURP-FtSG8ubh0328gXB5SNZCUdmX8d9ukC53lnDPzJj5sa_XbyIufE7kSTi6_HYb4zO0A6RHavdPY27rMSA-FnnTQqaf8up3u30ENo-5rwVQqTBuwnKHQBouQVulgXImu7BFWY-BgYnLMSCccgrLZAIsMQEry-QLIazb8:1uNAKF:YBZJpl16mb4l4-FPPVcQhibUgj3mu8P3pedF5whM1qM', '2025-06-19 13:08:07.059360'),
('fewrl74d7aokgp24rnqep4gbfw0lblzq', '.eJxVjDEOwjAMRe-SGUWO09SBkZ0zVE5sSAGlUtNOiLtDpQ6w_vfef5mB16UMa9N5GMWcDJrD75Y4P7RuQO5cb5PNU13mMdlNsTtt9jKJPs-7-3dQuJVv7ZCw67sA1B2BKPfgxANTQAeQI6gkjYkAk4BHT5xY6CqoIYagUc37A59CNvw:1uNPck:41OmDXyrqNMl4frurlpmOM8yXMCTKSu1jNS5H2O9wXw', '2025-06-20 05:28:14.158662'),
('q5ee8d8ap1zj0r9nkimdjjopr1meahrc', 'e30:1uPeCd:4lXJlbF_GI_qMyNnYIiR1V99DxPvI85NBaLMYbkZnZc', '2025-06-26 09:26:31.779299');

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_earnings`
--

CREATE TABLE `vehicles_earnings` (
  `id` bigint(20) NOT NULL,
  `owner_earnings` decimal(10,2) NOT NULL,
  `platform_commission` decimal(10,2) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `paid_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `rental_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicles_earnings`
--

INSERT INTO `vehicles_earnings` (`id`, `owner_earnings`, `platform_commission`, `payment_status`, `paid_at`, `created_at`, `updated_at`, `rental_id`) VALUES
(7, 135.00, 15.00, 'PENDING', NULL, '2025-06-12 05:10:43.461370', '2025-06-12 05:10:43.461387', 21),
(8, 9000.00, 1000.00, 'PAID', '2025-06-12 05:36:10.000000', '2025-06-12 05:32:47.274885', '2025-06-12 05:36:13.706062', 22),
(9, 5400.00, 600.00, 'PENDING', NULL, '2025-06-12 06:10:12.475232', '2025-06-12 08:41:27.187530', 23),
(10, 342.00, 38.00, 'PENDING', NULL, '2025-06-12 06:46:28.495731', '2025-06-12 08:51:16.021237', 24),
(11, 16200.00, 1800.00, 'PENDING', NULL, '2025-06-12 09:06:30.557113', '2025-06-12 09:06:30.557129', 25),
(12, 202.50, 22.50, 'PENDING', NULL, '2025-06-14 07:04:13.812122', '2025-06-14 07:04:13.812137', 26),
(13, 2070.00, 230.00, 'PENDING', NULL, '2025-06-14 07:07:21.296655', '2025-06-14 07:07:21.296675', 27);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_location`
--

CREATE TABLE `vehicles_location` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `latitude` decimal(9,6) DEFAULT NULL,
  `longitude` decimal(9,6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicles_location`
--

INSERT INTO `vehicles_location` (`id`, `name`, `address`, `latitude`, `longitude`) VALUES
(9, 'President,Roxas Capiz', '123 Downtown St, New York, NY', 40.712800, -74.006000),
(10, 'Ivisan,Capiz', '456 Uptown Ave, New York, NY', 40.783100, -73.971200),
(11, 'Roxas,City Capiz', '789 Midtown Blvd, New York, NY', 40.754900, -73.984000);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_rental`
--

CREATE TABLE `vehicles_rental` (
  `id` bigint(20) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `total_cost` decimal(10,2) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `renter_id` bigint(20) NOT NULL,
  `vehicle_id` bigint(20) NOT NULL,
  `commission_rate` decimal(4,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicles_rental`
--

INSERT INTO `vehicles_rental` (`id`, `start_date`, `end_date`, `total_cost`, `is_active`, `created_at`, `renter_id`, `vehicle_id`, `commission_rate`) VALUES
(21, '2025-06-13', '2025-06-15', 150.00, 0, '2025-06-12 05:10:43.453367', 2, 12, 10.00),
(22, '2025-06-18', '2025-06-23', 10000.00, 0, '2025-06-12 05:32:47.261708', 2, 16, 10.00),
(23, '2025-06-12', '2025-06-15', 6000.00, 1, '2025-06-12 06:10:12.457654', 14, 15, 10.00),
(24, '2025-06-12', '2025-06-16', 380.00, 1, '2025-06-12 06:46:28.492909', 14, 13, 10.00),
(25, '2025-06-13', '2025-06-22', 18000.00, 1, '2025-06-12 09:06:30.547879', 2, 16, 10.00),
(26, '2025-06-20', '2025-06-23', 225.00, 1, '2025-06-14 07:04:13.803248', 2, 12, 10.00),
(27, '2025-06-14', '2025-06-15', 2300.00, 1, '2025-06-14 07:07:21.279251', 14, 14, 10.00);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles_vehicle`
--

CREATE TABLE `vehicles_vehicle` (
  `id` bigint(20) NOT NULL,
  `make` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `year` int(10) UNSIGNED NOT NULL CHECK (`year` >= 0),
  `vehicle_type` varchar(15) NOT NULL,
  `daily_rate` decimal(10,2) NOT NULL,
  `is_available` tinyint(1) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `owner_id` bigint(20) NOT NULL,
  `location_id` bigint(20) DEFAULT NULL,
  `latitude` decimal(9,6) DEFAULT NULL,
  `location_address` varchar(255) DEFAULT NULL,
  `longitude` decimal(9,6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicles_vehicle`
--

INSERT INTO `vehicles_vehicle` (`id`, `make`, `model`, `year`, `vehicle_type`, `daily_rate`, `is_available`, `image`, `description`, `created_at`, `updated_at`, `owner_id`, `location_id`, `latitude`, `location_address`, `longitude`) VALUES
(12, 'Toyota', 'Camry', 2022, 'SEDAN', 75.00, 0, 'vehicle_images/avanza.png', 'Test vehicle at Downtown', '2025-06-12 04:49:48.612581', '2025-06-14 07:04:13.822767', 17, 9, 40.712800, '123 Downtown St, New York, NY', -74.006000),
(13, 'Honda', 'CR-V', 2023, 'SUV', 95.00, 0, 'vehicle_images/Honda_srv.png', 'Test vehicle at Uptown', '2025-06-12 04:49:48.621287', '2025-06-12 06:46:28.497538', 17, 9, 40.783100, '456 Uptown Ave, New York, NY', -73.971200),
(14, 'Tesla', 'Model 3', 2023, 'ELECTRIC', 2300.00, 0, 'vehicle_images/tesla.png', 'Test vehicle at Midtown', '2025-06-12 04:49:48.631203', '2025-06-14 07:07:21.303563', 2, 9, 40.754900, '789 Midtown Blvd, New York, NY', -73.984000),
(15, 'Hyundai', 'Stargazer', 2024, 'SUV', 2000.00, 0, 'vehicle_images/Stargazer_HymrNDv.png', '5 Seater', '2025-06-12 05:13:08.213584', '2025-06-12 06:10:12.480769', 2, 10, NULL, NULL, NULL),
(16, 'Ford', 'Raptor', 2023, 'TRUCK', 2000.00, 0, 'vehicle_images/Raptor.png', '4 seaters', '2025-06-12 05:32:31.406927', '2025-06-12 09:06:30.559016', 2, 10, NULL, NULL, NULL),
(17, 'Mercedes Benz', 'GLC', 2023, 'SUV', 15000.00, 1, 'vehicle_images/GLC.png', '5 seaters', '2025-06-12 05:46:52.326092', '2025-06-12 05:46:52.326111', 2, NULL, NULL, NULL, NULL),
(18, 'Porsche', '911 Carrera', 2024, 'SPORTS', 50000.00, 1, 'vehicle_images/porche_6pqvHP2.png', '2 Seaters', '2025-06-12 09:13:57.949681', '2025-06-12 09:13:57.949698', 2, NULL, NULL, NULL, NULL),
(19, 'Porsche', '911 Carrera', 2024, 'SPORTS', 5000.00, 1, 'vehicle_images/porche_dOp0mus.png', '2 Seaters', '2025-06-12 09:18:20.396718', '2025-06-12 09:18:20.396735', 2, NULL, NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `core_user`
--
ALTER TABLE `core_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `core_user_groups`
--
ALTER TABLE `core_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  ADD KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  ADD KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_core_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `vehicles_earnings`
--
ALTER TABLE `vehicles_earnings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `rental_id` (`rental_id`);

--
-- Indexes for table `vehicles_location`
--
ALTER TABLE `vehicles_location`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `vehicles_rental`
--
ALTER TABLE `vehicles_rental`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicles_rental_renter_id_5432f03d_fk_core_user_id` (`renter_id`),
  ADD KEY `vehicles_rental_vehicle_id_097fb0bf_fk_vehicles_vehicle_id` (`vehicle_id`);

--
-- Indexes for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicles_vehicle_owner_id_237ceed5_fk_core_user_id` (`owner_id`),
  ADD KEY `vehicles_vehicle_location_id_dd350e9a_fk_vehicles_location_id` (`location_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `core_user`
--
ALTER TABLE `core_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `core_user_groups`
--
ALTER TABLE `core_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `vehicles_earnings`
--
ALTER TABLE `vehicles_earnings`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `vehicles_location`
--
ALTER TABLE `vehicles_location`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `vehicles_rental`
--
ALTER TABLE `vehicles_rental`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `core_user_groups`
--
ALTER TABLE `core_user_groups`
  ADD CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Constraints for table `core_user_user_permissions`
--
ALTER TABLE `core_user_user_permissions`
  ADD CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`);

--
-- Constraints for table `vehicles_earnings`
--
ALTER TABLE `vehicles_earnings`
  ADD CONSTRAINT `vehicles_earnings_rental_id_3b48d372_fk_vehicles_rental_id` FOREIGN KEY (`rental_id`) REFERENCES `vehicles_rental` (`id`);

--
-- Constraints for table `vehicles_rental`
--
ALTER TABLE `vehicles_rental`
  ADD CONSTRAINT `vehicles_rental_renter_id_5432f03d_fk_core_user_id` FOREIGN KEY (`renter_id`) REFERENCES `core_user` (`id`),
  ADD CONSTRAINT `vehicles_rental_vehicle_id_097fb0bf_fk_vehicles_vehicle_id` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles_vehicle` (`id`);

--
-- Constraints for table `vehicles_vehicle`
--
ALTER TABLE `vehicles_vehicle`
  ADD CONSTRAINT `vehicles_vehicle_location_id_dd350e9a_fk_vehicles_location_id` FOREIGN KEY (`location_id`) REFERENCES `vehicles_location` (`id`),
  ADD CONSTRAINT `vehicles_vehicle_owner_id_237ceed5_fk_core_user_id` FOREIGN KEY (`owner_id`) REFERENCES `core_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
