-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema shopping_cart
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema shopping_cart
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shopping_cart` DEFAULT CHARACTER SET utf8 ;
USE `shopping_cart` ;

-- -----------------------------------------------------
-- Table `shopping_cart`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_cart`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `userName` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `shopping_cart`.`Cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_cart`.`Cart` (
  `cartID` INT NOT NULL AUTO_INCREMENT,
  `deliveryDate` DATETIME NULL,
  `cartStatus` INT NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`cartID`),
  INDEX `fk_table2_table1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_table2_table1`
    FOREIGN KEY (`User_id`)
    REFERENCES `shopping_cart`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `shopping_cart`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_cart`.`Category` (
  `idCategory` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  PRIMARY KEY (`idCategory`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `shopping_cart`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_cart`.`Product` (
  `idProduct` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Price` FLOAT NULL,
  `Category_idCategory` INT NOT NULL,
  PRIMARY KEY (`idProduct`),
  INDEX `fk_Product_Category1_idx` (`Category_idCategory` ASC) VISIBLE,
  CONSTRAINT `fk_Product_Category1`
    FOREIGN KEY (`Category_idCategory`)
    REFERENCES `shopping_cart`.`Category` (`idCategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `shopping_cart`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_cart`.`Order` (
  `idOrder` INT NOT NULL AUTO_INCREMENT,
  `Quantity` FLOAT NULL,
  `Product_idProduct` INT NOT NULL,
  `Cart_cartID` INT NOT NULL,
  PRIMARY KEY (`idOrder`),
  INDEX `fk_Order_Product1_idx` (`Product_idProduct` ASC) VISIBLE,
  INDEX `fk_Order_Cart1_idx` (`Cart_cartID` ASC) VISIBLE,
  CONSTRAINT `fk_Order_Product1`
    FOREIGN KEY (`Product_idProduct`)
    REFERENCES `shopping_cart`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Order_Cart1`
    FOREIGN KEY (`Cart_cartID`)
    REFERENCES `shopping_cart`.`Cart` (`cartID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
