-- This script creates the table hbtn_0d_usa with table states

-- Create the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Use the database hbtn_0d_usa
USE `hbtn_0d_usa`;

-- Create the table states
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY (`id`)
);
