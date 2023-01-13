-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: attendance check
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `id` text,
  `date` text,
  `check_in` text,
  `check_out` text,
  `outing` text,
  `comeback` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES ('abcd','2022-10-25','09:00','17:01','',''),('abcd','2022-10-27','09:00','17:01','',''),('abcd','2022-10-28','09:00','17:01','',''),('abcd','2022-10-31','09:00','17:01','',''),('abcd','2022-11-01','09:00','17:01','',''),('abcd','2022-11-02','09:00','17:01','',''),('abcd','2022-11-03','09:00','17:01','',''),('abcd','2022-11-04','09:00','17:01','',''),('abcd','2022-11-07','09:00','17:01','',''),('abcd','2022-11-08','09:00','17:01','',''),('abcd','2022-11-09','09:00','17:01','',''),('abcd','2022-11-10','09:00','17:01','',''),('abcd','2022-11-11','09:00','17:01','',''),('abcd','2022-11-14','09:00','17:01','',''),('abcd','2022-11-15','09:00','17:01','',''),('abcd','2022-11-16','09:00','17:01','',''),('abcd','2022-11-17','09:00','17:01','',''),('abcd','2022-11-18','09:00','17:01','',''),('abcd','2022-11-21','09:00','17:01','',''),('abcd','2022-11-22','09:00','17:01','',''),('abcd','2022-11-23','09:00','17:01','',''),('abcd','2022-11-24','09:00','17:01','',''),('abcd','2022-11-25','09:00','17:01','',''),('abcd','2022-11-28','09:00','17:01','',''),('abcd','2022-11-29','09:00','17:01','',''),('abcd','2022-11-30','09:00','17:01','',''),('abcd','2022-12-01','09:00','17:01','',''),('abcd','2022-12-02','09:00','17:01','',''),('abcd','2022-12-05','09:00','17:01','',''),('abcd','2022-12-12','09:00','17:01','',''),('abcd','2022-12-13','09:00','17:01','',''),('abcd','2022-12-14','09:00','17:01','',''),('abcd','2022-12-15','09:00','17:01','',''),('abcd','2022-12-16','09:00','17:01','',''),('abcd','2022-12-19','09:00','17:01','',''),('abcd','2022-12-20','09:00','17:01','',''),('abcd','2022-12-21','09:00','17:01','',''),('abcd','2022-12-22','09:00','17:01','',''),('abcd','2022-12-23','09:00','17:01','',''),('abcd','2023-01-02','09:00','17:01','',''),('abcd','2023-01-03','09:00','17:01','',''),('abcd','2023-01-04','09:00','17:01','',''),('abcd','2023-01-05','09:00','17:01','',''),('abcd','2023-01-06','09:00','17:01','',''),('abcd','2023-01-09','09:00','17:01','',''),('abcd','2023-01-10','09:00','16:59','',''),('abcd','2022-10-26','09:00','','',''),('abcd','2023-01-11','09:00','','',''),('abcd','2023-01-12','08:59','20:47','20:47','20:47'),('abcd','2023-01-13','19:00','19:02','19.02','19.02'),('abcd','2023-01-13','19:00','19:02','19.02','19.02'),('abcd','2023-01-13','','19:02','19.02','19.02'),('abcd','2023-01-13','','19:02','19.02','19.02'),('abcd','2023-01-13','','','','');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-13 20:55:18
