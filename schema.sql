CREATE DATABASE `nsinteriors`;

USE `nsinteriors`;

CREATE TABLE `comments` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100),
  `email` VARCHAR(100),
  `message` MEDIUMTEXT,
  `created_date` DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE `query` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100),
  `email` VARCHAR(100),
  `query` MEDIUMTEXT,
  `created_date` DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE `image_category` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `image_for` VARCHAR(100),
  `created_date` DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO image_category (image_for) VALUES ("project gallery");
INSERT INTO image_category (image_for) VALUES ("budget projects");


CREATE TABLE `image` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `image_name` VARCHAR(100),
  `image_for` int,
  `created_date` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`image_for`) REFERENCES `image_category`(`id`)
);

INSERT INTO image (image_name, image_for) VALUES ("IMG_7061.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7092.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7214.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7104.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7133.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7145.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7159.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7197.jpg",1);
INSERT INTO image (image_name, image_for) VALUES ("IMG_7142.jpg",1);