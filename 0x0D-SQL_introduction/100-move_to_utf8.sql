-- This script converts the `hbtn_0c_0` database to UTF8 in MySQL Server.

-- Switch to the `hbtn_0c_0` database
USE hbtn_0c_0;

-- Alter the database character set and collation
-- Set the character set to utf8mb4 and collation to utf8mb4_unicode_ci
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the table character set and collation
-- Convert the `first_table` table to character set utf8mb4 and collation utf8mb4_unicode_ci
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
