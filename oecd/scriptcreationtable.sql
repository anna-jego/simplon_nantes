-- MySQL Script generated by MySQL Workbench
-- Thu Mar  5 11:57:19 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema oecd
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema oecd
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `oecd` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `oecd` ;

-- -----------------------------------------------------
-- Table `oecd`.`continents`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oecd`.`continents` (
  `id` INT(11) NOT NULL,
  `continents` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `oecd`.`appartenir`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oecd`.`appartenir` (
  `id` INT(11) NULL DEFAULT NULL,
  `noms_pays` VARCHAR(30) NULL DEFAULT NULL,
  `PIB` VARCHAR(30) NULL DEFAULT NULL,
  `indicateur_vivre_mieux` VARCHAR(30) NULL DEFAULT NULL,
  `continents_id` INT(11) NOT NULL,
  PRIMARY KEY (`continents_id`),
  CONSTRAINT `fk_appartenir_continents`
    FOREIGN KEY (`continents_id`)
    REFERENCES `oecd`.`continents` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `oecd`.`oecd`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `oecd`.`oecd` (
  `id` INT(11) NULL DEFAULT NULL,
  `noms_pays` VARCHAR(30) NULL DEFAULT NULL,
  `PIB` VARCHAR(30) NULL DEFAULT NULL,
  `indicateur_vivre_mieux` VARCHAR(30) NULL DEFAULT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
