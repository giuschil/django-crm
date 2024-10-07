-- MySQL dump 10.13  Distrib 8.0.30, for macos12 (arm64)
--
-- Host: localhost    Database: crm
-- ------------------------------------------------------
-- Server version	8.0.30

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
-- Table structure for table `website_clients`
--

DROP TABLE IF EXISTS `website_clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `website_clients` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `role` varchar(50) NOT NULL,
  `city` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `website_clients`
--

LOCK TABLES `website_clients` WRITE;
/*!40000 ALTER TABLE `website_clients` DISABLE KEYS */;
INSERT INTO `website_clients` VALUES (10,'Gracea','Lee','grace.lee@example.com','Admin','Rome','IT','client_images/foto-profilo.jpg'),(11,'Hank','Pym','hank.pym@example.com','Moderator',NULL,'IT',NULL),(12,'Ivy','Walker','ivy.walker@example.com','Admin','Milan','IT',NULL),(13,'John','Doe','john.doe@example.com','User','Napoli','IT',NULL),(14,'Giuseppe','Giuseppe','gg@gg.it','prova','Milan','IT',NULL),(15,'test','test','test@email.it','test','test','test',NULL),(16,'Giuseppe','Schillaci','giuschil@gmail.com','prova','SALERNO','Italia',NULL),(17,'Mario','Rossi','mario.rossi@example.com','Admin','Roma','Italia',NULL),(18,'Luigi','Bianchi','luigi.bianchi@example.com','User','Milano','Italia',NULL),(19,'Giulia','Verdi','giulia.verdi@example.com','Manager','Napoli','Italia',NULL),(20,'Francesca','Neri','francesca.neri@example.com','User','Torino','Italia',NULL),(21,'Alessandro','Gialli','alessandro.gialli@example.com','Admin','Firenze','Italia',NULL),(22,'Marco','Blu','marco.blu@example.com','User','Genova','Italia',NULL),(23,'Elena','Viola','elena.viola@example.com','Manager','Bologna','Italia',NULL),(24,'Paolo','Arancio','paolo.arancio@example.com','User','Venezia','Italia',NULL),(25,'Sara','Rosa','sara.rosa@example.com','Admin','Palermo','Italia',NULL),(26,'Giorgio','Marrone','giorgio.marrone@example.com','User','Catania','Italia',NULL),(27,'Laura','Verde','laura.verde@example.com','Manager','Verona','Italia',NULL),(28,'Davide','Nero','davide.nero@example.com','User','Trieste','Italia',NULL),(29,'Chiara','Bianco','chiara.bianco@example.com','Admin','Parma','Italia',NULL),(30,'Federico','Grigio','federico.grigio@example.com','User','Perugia','Italia',NULL),(31,'Martina','Giallo','martina.giallo@example.com','Manager','Ancona','Italia',NULL),(32,'Simone','Azzurro','simone.azzurro@example.com','User','Pisa','Italia',NULL),(33,'Valentina','Rosso','valentina.rosso@example.com','Admin','Siena','Italia',NULL),(34,'Andrea','Viola','andrea.viola@example.com','User','Rimini','Italia',NULL),(35,'Claudia','Verde','claudia.verde@example.com','Manager','Lecce','Italia','client_images/fronte_JhNTjML.png'),(36,'Matteoo','Blu','matteo.blu@example.com','User','Bari','Italia','client_images/fronte_rH7PI50.png'),(37,'Antonio','Scem','scem@gmail.com','User','SALERNO','Italia',''),(38,'ciao','ciao','ciao@test.it','User','Milan','IT',''),(39,'Antonio','Schillaci','giuschil@gmail.com','Admin','SALERNO','Italia',''),(67,'test','test','giuschil@gmail.com','prova','SALERNO','Italia','');
/*!40000 ALTER TABLE `website_clients` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-04 21:50:08
