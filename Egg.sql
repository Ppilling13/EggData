
USE egg_data_db;

CREATE TABLE Egg_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Eggs decimal(10,2) NOT NULL,
    Deaths decimal(10,2) NOT NULL,
    date_collected DATE NOT NULL
);
 drop table manual_observations;
 select * from Egg_data;
 
show databases;

use egg_data_db;
show tables;

select * from egg_data;
commit;
