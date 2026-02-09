
Кейс задача - 1 
Сумма отрицательных элементов между максимальным и минимальным.  
(test1.py)
n = int(input("Введите количество элементов массива 'A': "))
arr = []

print("Введите элементы массива:")
for i in range(n):
 arr.append(float(input()))

min_i = arr.index(min(arr))
max_i = arr.index(max(arr))

start = min(min_i, max_i) + 1
end = max(min_i, max_i)

result = sum(x for x in arr[start:end] if x < 0)

print("Сумма отрицательных элементов между min и max =", result)


Кейс задача - 2 
Демонстрация работы методов базового и производного класса.  
(tesstcase2.py)

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def info(self):
        print(f"Сотрудник: {self.name}")
        print(f"Базовая зарплата: {self.base_salary} евро.")

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, base_salary, languages):
        super().__init__(name, base_salary)
        self.languages = languages

    def info(self):
        super().info()
        print(f"Языки программирования: {', '.join(self.languages)}")

    def calculate_salary(self):
        bonus = 500 * len(self.languages)
        return self.base_salary + bonus

    def write_code(self):
        print(f"{self.name} Разрабатывает ПО")


class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def info(self):
        super().info()
        print(f"Размер команды: {self.team_size} человек")

    def calculate_salary(self):
        bonus = self.team_size * 300
        return self.base_salary + bonus

    def hold_meeting(self):
        print(f"{self.name} Контролирует работу команды разработчиков")


def main():
    print("\nВведите данные программиста")
    dev_name = input("Имя: ")
    dev_salary = int(input("Базовая зарплата: "))
    langs = input("Введите языки через запятую: ").split(",")
    langs = [l.strip() for l in langs]

    dev = Developer(dev_name, dev_salary, langs)

    print("\nВведите данные управляющего")
    mgr_name = input("Имя: ")
    mgr_salary = int(input("Базовая зарплата: "))
    team_size = int(input("Размер команды: "))

    mgr = Manager(mgr_name, mgr_salary, team_size)

    print("\nПрограммист")
    dev.info()
    print("Итоговая зарплата:", dev.calculate_salary(), "евро.")
    dev.write_code()

    print("\nУправляющий")
    mgr.info()
    print("Итоговая зарплата:", mgr.calculate_salary(), "евро.")
    mgr.hold_meeting()


if __name__ == "__main__":
    main()

Кейс задача - 3
База данных «Туризм»  
(туризм2.sql)


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def info(self):
        print(f"Сотрудник: {self.name}")
        print(f"Базовая зарплата: {self.base_salary} евро.")

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    def __init__(self, name, base_salary, languages):
        super().__init__(name, base_salary)
        self.languages = languages

    def info(self):
        super().info()
        print(f"Языки программирования: {', '.join(self.languages)}")

    def calculate_salary(self):
        bonus = 500 * len(self.languages)
        return self.base_salary + bonus

    def write_code(self):
        print(f"{self.name} Разрабатывает ПО")


class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = team_size

    def info(self):
        super().info()
        print(f"Размер команды: {self.team_size} человек")

    def calculate_salary(self):
        bonus = self.team_size * 300
        return self.base_salary + bonus

    def hold_meeting(self):
        print(f"{self.name} Контролирует работу команды разработчиков")


def main():
    print("\nВведите данные программиста")
    dev_name = input("Имя: ")
    dev_salary = int(input("Базовая зарплата: "))
    langs = input("Введите языки через запятую: ").split(",")
    langs = [l.strip() for l in langs]

    dev = Developer(dev_name, dev_salary, langs)

    print("\nВведите данные управляющего")
    mgr_name = input("Имя: ")
    mgr_salary = int(input("Базовая зарплата: "))
    team_size = int(input("Размер команды: "))

    mgr = Manager(mgr_name, mgr_salary, team_size)

    print("\nПрограммист")
    dev.info()
    print("Итоговая зарплата:", dev.calculate_salary(), "евро.")
    dev.write_code()

    print("\nУправляющий")
    mgr.info()



    Тест кейс 4 
    unit Кейс4;

interface

uses
  System.SysUtils, System.Classes, Web.HTTPApp, FireDAC.Stan.Intf,
  FireDAC.Stan.Option, FireDAC.Stan.Error, FireDAC.UI.Intf, FireDAC.Phys.Intf,
  FireDAC.Stan.Def, FireDAC.Stan.Pool, FireDAC.Stan.Async, FireDAC.Phys,
  FireDAC.Phys.MySQL, FireDAC.Phys.MySQLDef, FireDAC.ConsoleUI.Wait,
  FireDAC.Stan.Param, FireDAC.DatS, FireDAC.DApt.Intf, FireDAC.DApt,
  Web.HTTPProd, Data.DB, FireDAC.Comp.DataSet, FireDAC.Comp.Client;

type
  TWebModule1 = class(TWebModule)
    FDConnection1: TFDConnection;
    FDQuery1: TFDQuery;
    FDPhysMySQLDriverLink1: TFDPhysMySQLDriverLink;
    PageProducer1: TPageProducer;
    procedure WebModule1DefaultHandlerAction(Sender: TObject;
      Request: TWebRequest; Response: TWebResponse; var Handled: Boolean);
    procedure PageProducer1HTMLTag(Sender: TObject; Tag: TTag;
      const TagString: string; TagParams: TStrings; var ReplaceText: string);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  WebModuleClass: TComponentClass = TWebModule1;

implementation

{%CLASSGROUP 'System.Classes.TPersistent'}

{$R *.dfm}


procedure TWebModule1.WebModule1DefaultHandlerAction(Sender: TObject;
  Request: TWebRequest; Response: TWebResponse; var Handled: Boolean);
begin
  Response.Content := PageProducer1.Content;
end;

procedure TWebModule1.PageProducer1HTMLTag(Sender: TObject; Tag: TTag;
  const TagString: string; TagParams: TStrings; var ReplaceText: string);
var
  S: string;
begin
  if TagString = 'ORDER_LIST' then
  begin
    try
      FDQuery1.Close;
      FDQuery1.Open;
      S := '';
      while not FDQuery1.Eof do
    begin
      S := S + '<tr>' +
        '<td>' + FDQuery1.FieldByName('idЗаказы').AsString + '</td>' +
        '<td>' + FDQuery1.FieldByName('Имя').AsString + ' ' + FDQuery1.FieldByName('Фамилия').AsString + '</td>' +
        '<td>' + FDQuery1.FieldByName('Отель').AsString + '</td>' +
        '<td>' + FDQuery1.FieldByName('Страна').AsString + '</td>' +
        '<td>' + FDQuery1.FieldByName('Экскурсия').AsString + '</td>' +
        '<td>' + FDQuery1.FieldByName('Цена').AsString + ' €</td>' +
        '<td>' + FDQuery1.FieldByName('order_date').AsString + '</td>' +
        '</tr>';
      FDQuery1.Next;
    end;
      ReplaceText := S;
    except
      on E: Exception do
        ReplaceText := '<tr><td colspan="6">Ошибка БД: ' + E.Message + '</td></tr>';
    end;
  end;
end;

end.

БД
-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: tourism_new
-- ------------------------------------------------------
-- Server version	9.6.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '515f8000-fea5-11f0-bc28-025094a5a523:1-168';

--
-- Table structure for table `заказы`
--

DROP TABLE IF EXISTS `заказы`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `заказы` (
  `idЗаказы` int NOT NULL AUTO_INCREMENT,
  `idКлиенты` int NOT NULL,
  `idОтели` int NOT NULL,
  `idЭкскурссии` int NOT NULL,
  `order_date` date NOT NULL,
  PRIMARY KEY (`idЗаказы`),
  KEY `Клиенты_idx` (`idКлиенты`),
  KEY `Отели_idx` (`idОтели`),
  KEY `Экскурссии_idx` (`idЭкскурссии`),
  CONSTRAINT `Клиенты` FOREIGN KEY (`idКлиенты`) REFERENCES `клиенты` (`idКлиенты`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Отели` FOREIGN KEY (`idОтели`) REFERENCES `отели` (`idОтели`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Экскурссии` FOREIGN KEY (`idЭкскурссии`) REFERENCES `экскурссии` (`idЭкскурссии`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `заказы`
--

LOCK TABLES `заказы` WRITE;
/*!40000 ALTER TABLE `заказы` DISABLE KEYS */;
INSERT INTO `заказы` VALUES (1,1,2,1,'2026-02-15'),(2,2,1,3,'2026-03-07'),(3,3,3,2,'2026-08-25');
/*!40000 ALTER TABLE `заказы` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `клиенты`
--

DROP TABLE IF EXISTS `клиенты`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `клиенты` (
  `idКлиенты` int NOT NULL AUTO_INCREMENT,
  `Имя` varchar(45) NOT NULL,
  `Фамилия` varchar(45) NOT NULL,
  PRIMARY KEY (`idКлиенты`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `клиенты`
--

LOCK TABLES `клиенты` WRITE;
/*!40000 ALTER TABLE `клиенты` DISABLE KEYS */;
INSERT INTO `клиенты` VALUES (1,'Иво','Темперсе'),(2,'Иван','Авгеев'),(3,'Бен','Биггович');
/*!40000 ALTER TABLE `клиенты` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `отели`
--

DROP TABLE IF EXISTS `отели`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `отели` (
  `idОтели` int NOT NULL AUTO_INCREMENT,
  `Название` varchar(45) NOT NULL,
  `idСтраны` int NOT NULL,
  PRIMARY KEY (`idОтели`),
  CONSTRAINT `Страны` FOREIGN KEY (`idОтели`) REFERENCES `страны` (`idСтраны`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `отели`
--

LOCK TABLES `отели` WRITE;
/*!40000 ALTER TABLE `отели` DISABLE KEYS */;
INSERT INTO `отели` VALUES (1,'Москвич',1),(2,'Балтика',2),(3,'Роял',3);
/*!40000 ALTER TABLE `отели` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `страны`
--

DROP TABLE IF EXISTS `страны`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `страны` (
  `idСтраны` int NOT NULL AUTO_INCREMENT,
  `Страна` varchar(45) NOT NULL,
  PRIMARY KEY (`idСтраны`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `страны`
--

LOCK TABLES `страны` WRITE;
/*!40000 ALTER TABLE `страны` DISABLE KEYS */;
INSERT INTO `страны` VALUES (1,'Россия'),(2,'Эстония'),(3,'Англия');
/*!40000 ALTER TABLE `страны` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `экскурссии`
--

DROP TABLE IF EXISTS `экскурссии`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `экскурссии` (
  `idЭкскурссии` int NOT NULL AUTO_INCREMENT,
  `Название` varchar(45) NOT NULL,
  `Цена` decimal(10,2) NOT NULL,
  PRIMARY KEY (`idЭкскурссии`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `экскурссии`
--

LOCK TABLES `экскурссии` WRITE;
/*!40000 ALTER TABLE `экскурссии` DISABLE KEYS */;
INSERT INTO `экскурссии` VALUES (1,'Подводная охота',300.00),(2,'Полетать на вертолете',150.00),(3,'История города',50.00);
/*!40000 ALTER TABLE `экскурссии` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-09 13:11:03

    print("Итоговая зарплата:", mgr.calculate_salary(), "евро.")
    mgr.hold_meeting()


if __name__ == "__main__":
    main()
