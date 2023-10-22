-- Converts database to UTF8mb4_unicode_ci
USE `hbtn_0c_0`;
ALTER TABLE `first_table` 
	MODIFY `name` VARCHAR(256); 
ALTER TABLE `first_table` COLLATE 'utf8mb4_unicode_ci';
ALTER DATABASE `hbtn_0c_0` COLLATE 'utf8mb4_unicode_ci';
