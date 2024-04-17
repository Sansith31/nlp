CREATE DATABASE sdms;


CREATE TABLE student
(
    studentid INT NOT NULL,
    studentname VARCHAR(20),
    dob DATE,
    gender VARCHAR(1),
    contact INT,
    email VARCHAR(50),
    pathway VARCHAR(50),
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

INSERT INTO pathway
VALUES ("Computer Science", "Programming Fundamentals", "Web Designing", "Mathematics for Computing", "Networking Fundamentals"),
("Software Engineering", "Programming Fundamentals", "Web Designing", "Software Development", "Networking Fundamentals"),
("Data Science", "Programming Fundamentals", "Working with Data", "Mathematics for Data Science", "Data Structures and Algorithms"),
("Business Management", "Introduction to Economics", "Project Management", "Mathematics for Business", "Marketing");