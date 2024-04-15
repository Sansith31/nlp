CREATE DATABASE sdms;


CREATE TABLE student
(
    studentid INT NOT NULL,
    studentname VARCHAR(20),
    dob DATE,
    gender VARCHAR(1),
    contact INT,
    email VARCHAR(50),
    pathway VARCHAR(10),
    PRIMARY KEY(studentid),
    FOREIGN KEY(pathway) REFERENCES pathway(pathwayname)
);

CREATE TABLE pathway
(
    pathwayname VARCHAR(20) NOT NULL,
    module1 VARCHAR(50),
    module2 VARCHAR(50),
    module3 VARCHAR(50),
    module4 VARCHAR(50),
    PRIMARY KEY(pathwayname)
);