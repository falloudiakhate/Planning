-- MySQL dump 10.13  Distrib 8.0.18, for Linux (x86_64)
--
-- Host: localhost    Database: PlanningDatabase
-- ------------------------------------------------------
-- Server version	8.0.18-0ubuntu0.19.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Accounts_cahier_de_texte`
--

DROP TABLE IF EXISTS `Accounts_cahier_de_texte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_cahier_de_texte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titre_EC` varchar(50) NOT NULL,
  `duree_EC` int(11) NOT NULL,
  `nom_professeur` int(11) NOT NULL,
  `contenu` longtext NOT NULL,
  `date` datetime(6) NOT NULL,
  `responsable_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_cahier_de_t_responsable_id_4b6ae438_fk_Accounts_` (`responsable_id`),
  CONSTRAINT `Accounts_cahier_de_t_responsable_id_4b6ae438_fk_Accounts_` FOREIGN KEY (`responsable_id`) REFERENCES `Accounts_responsable` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_cahier_de_texte`
--

LOCK TABLES `Accounts_cahier_de_texte` WRITE;
/*!40000 ALTER TABLE `Accounts_cahier_de_texte` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_cahier_de_texte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_chef_departement`
--

DROP TABLE IF EXISTS `Accounts_chef_departement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_chef_departement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `pseudo` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `num_professeur` int(11) NOT NULL,
  `num_chef_departement` int(11) NOT NULL,
  `Professeur_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_chef_depart_Professeur_id_476b6dfa_fk_Accounts_` (`Professeur_id`),
  KEY `Accounts_chef_depart_utilisateur_id_d625800c_fk_Accounts_` (`utilisateur_id`),
  CONSTRAINT `Accounts_chef_depart_Professeur_id_476b6dfa_fk_Accounts_` FOREIGN KEY (`Professeur_id`) REFERENCES `Accounts_professeur` (`id`),
  CONSTRAINT `Accounts_chef_depart_utilisateur_id_d625800c_fk_Accounts_` FOREIGN KEY (`utilisateur_id`) REFERENCES `Accounts_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_chef_departement`
--

LOCK TABLES `Accounts_chef_departement` WRITE;
/*!40000 ALTER TABLE `Accounts_chef_departement` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_chef_departement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_classe`
--

DROP TABLE IF EXISTS `Accounts_classe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_classe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `annee` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_classe`
--

LOCK TABLES `Accounts_classe` WRITE;
/*!40000 ALTER TABLE `Accounts_classe` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_classe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_dispenser_cours`
--

DROP TABLE IF EXISTS `Accounts_dispenser_cours`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_dispenser_cours` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `classe_id` int(11) NOT NULL,
  `professeur_id` int(11) NOT NULL,
  `uc_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_dispenser_c_classe_id_b81cd807_fk_Accounts_` (`classe_id`),
  KEY `Accounts_dispenser_c_professeur_id_031556ab_fk_Accounts_` (`professeur_id`),
  KEY `Accounts_dispenser_cours_uc_id_384bea7e_fk_Accounts_ec_id` (`uc_id`),
  CONSTRAINT `Accounts_dispenser_c_classe_id_b81cd807_fk_Accounts_` FOREIGN KEY (`classe_id`) REFERENCES `Accounts_classe` (`id`),
  CONSTRAINT `Accounts_dispenser_c_professeur_id_031556ab_fk_Accounts_` FOREIGN KEY (`professeur_id`) REFERENCES `Accounts_professeur` (`id`),
  CONSTRAINT `Accounts_dispenser_cours_uc_id_384bea7e_fk_Accounts_ec_id` FOREIGN KEY (`uc_id`) REFERENCES `Accounts_ec` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_dispenser_cours`
--

LOCK TABLES `Accounts_dispenser_cours` WRITE;
/*!40000 ALTER TABLE `Accounts_dispenser_cours` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_dispenser_cours` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_ec`
--

DROP TABLE IF EXISTS `Accounts_ec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_ec` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `charge_horaire` int(11) NOT NULL,
  `coef` int(11) NOT NULL,
  `ue_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_ec_ue_id_ef3e3765_fk_Accounts_ue_id` (`ue_id`),
  CONSTRAINT `Accounts_ec_ue_id_ef3e3765_fk_Accounts_ue_id` FOREIGN KEY (`ue_id`) REFERENCES `Accounts_ue` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_ec`
--

LOCK TABLES `Accounts_ec` WRITE;
/*!40000 ALTER TABLE `Accounts_ec` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_ec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_eleve`
--

DROP TABLE IF EXISTS `Accounts_eleve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_eleve` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `pseudo` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `num_eleve` int(11) NOT NULL,
  `classe_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_eleve_utilisateur_id_aab6ddcc_fk_Accounts_` (`utilisateur_id`),
  KEY `Accounts_eleve_classe_id_0e9b0288_fk_Accounts_classe_id` (`classe_id`),
  CONSTRAINT `Accounts_eleve_classe_id_0e9b0288_fk_Accounts_classe_id` FOREIGN KEY (`classe_id`) REFERENCES `Accounts_classe` (`id`),
  CONSTRAINT `Accounts_eleve_utilisateur_id_aab6ddcc_fk_Accounts_` FOREIGN KEY (`utilisateur_id`) REFERENCES `Accounts_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_eleve`
--

LOCK TABLES `Accounts_eleve` WRITE;
/*!40000 ALTER TABLE `Accounts_eleve` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_eleve` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_maquette`
--

DROP TABLE IF EXISTS `Accounts_maquette`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_maquette` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_maquette`
--

LOCK TABLES `Accounts_maquette` WRITE;
/*!40000 ALTER TABLE `Accounts_maquette` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_maquette` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_professeur`
--

DROP TABLE IF EXISTS `Accounts_professeur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_professeur` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `pseudo` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `num_professeur` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_professeur_utilisateur_id_8dfc19c4_fk_Accounts_` (`utilisateur_id`),
  CONSTRAINT `Accounts_professeur_utilisateur_id_8dfc19c4_fk_Accounts_` FOREIGN KEY (`utilisateur_id`) REFERENCES `Accounts_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_professeur`
--

LOCK TABLES `Accounts_professeur` WRITE;
/*!40000 ALTER TABLE `Accounts_professeur` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_professeur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_professeur_pedagogique`
--

DROP TABLE IF EXISTS `Accounts_professeur_pedagogique`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_professeur_pedagogique` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `pseudo` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `num_professeur` int(11) NOT NULL,
  `num_professeur_pedagogique` int(11) NOT NULL,
  `Professeur_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_professeur__utilisateur_id_da1799b7_fk_Accounts_` (`utilisateur_id`),
  KEY `Accounts_professeur__Professeur_id_18b3a8a2_fk_Accounts_` (`Professeur_id`),
  CONSTRAINT `Accounts_professeur__Professeur_id_18b3a8a2_fk_Accounts_` FOREIGN KEY (`Professeur_id`) REFERENCES `Accounts_professeur` (`id`),
  CONSTRAINT `Accounts_professeur__utilisateur_id_da1799b7_fk_Accounts_` FOREIGN KEY (`utilisateur_id`) REFERENCES `Accounts_utilisateur` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_professeur_pedagogique`
--

LOCK TABLES `Accounts_professeur_pedagogique` WRITE;
/*!40000 ALTER TABLE `Accounts_professeur_pedagogique` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_professeur_pedagogique` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_publication`
--

DROP TABLE IF EXISTS `Accounts_publication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_publication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `message` longtext NOT NULL,
  `professeur_pedagogique_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_publication_professeur_pedagogiq_46dae6cb_fk_Accounts_` (`professeur_pedagogique_id`),
  CONSTRAINT `Accounts_publication_professeur_pedagogiq_46dae6cb_fk_Accounts_` FOREIGN KEY (`professeur_pedagogique_id`) REFERENCES `Accounts_professeur_pedagogique` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_publication`
--

LOCK TABLES `Accounts_publication` WRITE;
/*!40000 ALTER TABLE `Accounts_publication` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_publication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_responsable`
--

DROP TABLE IF EXISTS `Accounts_responsable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_responsable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `pseudo` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `num_eleve` int(11) NOT NULL,
  `eleve_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_responsable_eleve_id_d52ecd9a_fk_Accounts_eleve_id` (`eleve_id`),
  CONSTRAINT `Accounts_responsable_eleve_id_d52ecd9a_fk_Accounts_eleve_id` FOREIGN KEY (`eleve_id`) REFERENCES `Accounts_eleve` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_responsable`
--

LOCK TABLES `Accounts_responsable` WRITE;
/*!40000 ALTER TABLE `Accounts_responsable` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_responsable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_time_table`
--

DROP TABLE IF EXISTS `Accounts_time_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_time_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime(6) NOT NULL,
  `document` varchar(100) NOT NULL,
  `professeur_pedagogique_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_time_table_professeur_pedagogiq_bf5d1bbe_fk_Accounts_` (`professeur_pedagogique_id`),
  CONSTRAINT `Accounts_time_table_professeur_pedagogiq_bf5d1bbe_fk_Accounts_` FOREIGN KEY (`professeur_pedagogique_id`) REFERENCES `Accounts_professeur_pedagogique` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_time_table`
--

LOCK TABLES `Accounts_time_table` WRITE;
/*!40000 ALTER TABLE `Accounts_time_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_time_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_ue`
--

DROP TABLE IF EXISTS `Accounts_ue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_ue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `code` varchar(50) NOT NULL,
  `maquette_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Accounts_ue_maquette_id_25e62fdb_fk_Accounts_maquette_id` (`maquette_id`),
  CONSTRAINT `Accounts_ue_maquette_id_25e62fdb_fk_Accounts_maquette_id` FOREIGN KEY (`maquette_id`) REFERENCES `Accounts_maquette` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_ue`
--

LOCK TABLES `Accounts_ue` WRITE;
/*!40000 ALTER TABLE `Accounts_ue` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_ue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Accounts_utilisateur`
--

DROP TABLE IF EXISTS `Accounts_utilisateur`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accounts_utilisateur` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `pseudo` varchar(50) NOT NULL,
  `telephone` varchar(50) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accounts_utilisateur`
--

LOCK TABLES `Accounts_utilisateur` WRITE;
/*!40000 ALTER TABLE `Accounts_utilisateur` DISABLE KEYS */;
/*!40000 ALTER TABLE `Accounts_utilisateur` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add maquette',7,'add_maquette'),(26,'Can change maquette',7,'change_maquette'),(27,'Can delete maquette',7,'delete_maquette'),(28,'Can view maquette',7,'view_maquette'),(29,'Can add ec',8,'add_ec'),(30,'Can change ec',8,'change_ec'),(31,'Can delete ec',8,'delete_ec'),(32,'Can view ec',8,'view_ec'),(33,'Can add ue',9,'add_ue'),(34,'Can change ue',9,'change_ue'),(35,'Can delete ue',9,'delete_ue'),(36,'Can view ue',9,'view_ue'),(37,'Can add chef_ departement',10,'add_chef_departement'),(38,'Can change chef_ departement',10,'change_chef_departement'),(39,'Can delete chef_ departement',10,'delete_chef_departement'),(40,'Can view chef_ departement',10,'view_chef_departement'),(41,'Can add eleve',11,'add_eleve'),(42,'Can change eleve',11,'change_eleve'),(43,'Can delete eleve',11,'delete_eleve'),(44,'Can view eleve',11,'view_eleve'),(45,'Can add cahier_ de_ texte',12,'add_cahier_de_texte'),(46,'Can change cahier_ de_ texte',12,'change_cahier_de_texte'),(47,'Can delete cahier_ de_ texte',12,'delete_cahier_de_texte'),(48,'Can view cahier_ de_ texte',12,'view_cahier_de_texte'),(49,'Can add publication',13,'add_publication'),(50,'Can change publication',13,'change_publication'),(51,'Can delete publication',13,'delete_publication'),(52,'Can view publication',13,'view_publication'),(53,'Can add responsable',14,'add_responsable'),(54,'Can change responsable',14,'change_responsable'),(55,'Can delete responsable',14,'delete_responsable'),(56,'Can view responsable',14,'view_responsable'),(57,'Can add utilisateur',15,'add_utilisateur'),(58,'Can change utilisateur',15,'change_utilisateur'),(59,'Can delete utilisateur',15,'delete_utilisateur'),(60,'Can view utilisateur',15,'view_utilisateur'),(61,'Can add time_ table',16,'add_time_table'),(62,'Can change time_ table',16,'change_time_table'),(63,'Can delete time_ table',16,'delete_time_table'),(64,'Can view time_ table',16,'view_time_table'),(65,'Can add professeur',17,'add_professeur'),(66,'Can change professeur',17,'change_professeur'),(67,'Can delete professeur',17,'delete_professeur'),(68,'Can view professeur',17,'view_professeur'),(69,'Can add classe',18,'add_classe'),(70,'Can change classe',18,'change_classe'),(71,'Can delete classe',18,'delete_classe'),(72,'Can view classe',18,'view_classe'),(73,'Can add professeur_ pedagogique',19,'add_professeur_pedagogique'),(74,'Can change professeur_ pedagogique',19,'change_professeur_pedagogique'),(75,'Can delete professeur_ pedagogique',19,'delete_professeur_pedagogique'),(76,'Can view professeur_ pedagogique',19,'view_professeur_pedagogique'),(77,'Can add dispenser_ cours',20,'add_dispenser_cours'),(78,'Can change dispenser_ cours',20,'change_dispenser_cours'),(79,'Can delete dispenser_ cours',20,'delete_dispenser_cours'),(80,'Can view dispenser_ cours',20,'view_dispenser_cours');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$PACvkhmyeQpb$r64TlBvI7hAKrfIEyukk16PVXPAz18ZkCTKdj7bbul8=','2020-01-29 11:37:07.738341',1,'falloudiakhate','','','dfallou@ept.sn',1,1,'2020-01-29 11:36:51.741945');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (12,'Accounts','cahier_de_texte'),(10,'Accounts','chef_departement'),(18,'Accounts','classe'),(20,'Accounts','dispenser_cours'),(8,'Accounts','ec'),(11,'Accounts','eleve'),(7,'Accounts','maquette'),(17,'Accounts','professeur'),(19,'Accounts','professeur_pedagogique'),(13,'Accounts','publication'),(14,'Accounts','responsable'),(16,'Accounts','time_table'),(9,'Accounts','ue'),(15,'Accounts','utilisateur'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-01-25 22:07:03.451285'),(2,'auth','0001_initial','2020-01-25 22:07:04.063433'),(3,'admin','0001_initial','2020-01-25 22:07:05.310783'),(4,'admin','0002_logentry_remove_auto_add','2020-01-25 22:07:05.672996'),(5,'admin','0003_logentry_add_action_flag_choices','2020-01-25 22:07:05.689249'),(6,'contenttypes','0002_remove_content_type_name','2020-01-25 22:07:05.964274'),(7,'auth','0002_alter_permission_name_max_length','2020-01-25 22:07:06.177807'),(8,'auth','0003_alter_user_email_max_length','2020-01-25 22:07:06.234847'),(9,'auth','0004_alter_user_username_opts','2020-01-25 22:07:06.252546'),(10,'auth','0005_alter_user_last_login_null','2020-01-25 22:07:06.394249'),(11,'auth','0006_require_contenttypes_0002','2020-01-25 22:07:06.405853'),(12,'auth','0007_alter_validators_add_error_messages','2020-01-25 22:07:06.429525'),(13,'auth','0008_alter_user_username_max_length','2020-01-25 22:07:06.584863'),(14,'auth','0009_alter_user_last_name_max_length','2020-01-25 22:07:06.740711'),(15,'auth','0010_alter_group_name_max_length','2020-01-25 22:07:06.793731'),(16,'auth','0011_update_proxy_permissions','2020-01-25 22:07:06.819426'),(17,'sessions','0001_initial','2020-01-25 22:07:06.890500'),(18,'Accounts','0001_initial','2020-01-29 11:17:11.311024'),(19,'Accounts','0002_dispenser_cours','2020-01-29 11:21:13.753153'),(20,'Accounts','0003_auto_20200129_1139','2020-01-29 11:40:04.529507'),(21,'Accounts','0004_auto_20200129_1154','2020-01-29 11:54:55.771371');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('jhl5lsok4ntwv5red5glq72tyyiz8tgv','MzFjNjc2NGJiMTBiOGU0MWNmY2UxNjIzZDQ2YTY4YzBjYjMwZGFiZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI3MTk4MjljYzY0NmI5Njg1OTI1NTVmZGU0MWRjOGYxYTcyOGI2NGUyIn0=','2020-02-12 11:37:07.750003');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-30 15:08:11
