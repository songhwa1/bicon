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
-- Table structure for table `data_ai2nd`
--

DROP TABLE IF EXISTS `data_ai2nd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data_ai2nd` (
  `번호` int DEFAULT NULL,
  `ID` text,
  `비밀번호` text,
  `이름` text,
  `구분` text,
  `클래스` text,
  `금일훈련` text,
  `입실` text,
  `복귀` text,
  `외출` text,
  `퇴실` text,
  `출석횟수` int DEFAULT NULL,
  `지각횟수` int DEFAULT NULL,
  `조퇴횟수` int DEFAULT NULL,
  `외출횟수` int DEFAULT NULL,
  `결석` int DEFAULT NULL,
  `출석일수` int DEFAULT NULL,
  `최대출석일수` int DEFAULT NULL,
  `과정진행` int DEFAULT NULL,
  `총과정진행` int DEFAULT NULL,
  `로그인여부` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_ai2nd`
--

LOCK TABLES `data_ai2nd` WRITE;
/*!40000 ALTER TABLE `data_ai2nd` DISABLE KEYS */;
INSERT INTO `data_ai2nd` VALUES (1,'','','강민영','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(2,'','','고연재','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(3,'','','김기태','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(4,'','','김명은','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(5,'ksi','1234','김성일','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,1,0,46,140,46,140,'O'),(6,'','','김연수','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(7,'','','노도현','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(8,'','','류가미','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(9,'','','박규환','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(10,'','','박성빈','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(11,'','','박시형','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(12,'','','박의용','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(13,'asdf','1234','오송화','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',4,6,1,4,0,46,140,46,140,'O'),(14,'','','이범규','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(15,'','','이보라','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(16,'','','이소윤','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(17,'','','이여름','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(18,'','','이지혜','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(19,'abcd','1234','이현도','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,48,48,49,2,46,140,46,140,'O'),(20,'','','임성경','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(21,'','','임영효','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(22,'','','임홍선','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(23,'','','장은희','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(24,'','','정연우','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(25,'','','정철우','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(26,'','','주민석','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(27,'','','최지혁','학생','데이터 기반 AI SW개발자 양성','','0','0','0','0',46,0,0,0,0,46,140,46,140,'X'),(100,'boki','1234','이상복','교수','데이터 기반 AI SW개발자 양성','','','','','',46,0,0,0,0,46,140,46,140,'X'),(101,'','','류홍걸','교수','데이터 기반 AI SW개발자 양성','','','','','',46,0,0,0,0,46,140,46,140,'X'),(102,'','','조동현','교수','데이터 기반 AI SW개발자 양성','','','','','',46,0,0,0,0,46,140,46,140,'X');
/*!40000 ALTER TABLE `data_ai2nd` ENABLE KEYS */;
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
