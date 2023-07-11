INSERT INTO dogs (name, breed, age)
VALUES ("Ringo", "Pomewawa", "10");

INSERT INTO dogs (name, breed, age)
VALUES ("Renly", "Who Knows???", "17");

# Order of arguments obviously matters; if you want to insert multiple entries at once, pass them as 'tuples' (not that SQL actually does tuples)

INSERT INTO dogs (name, breed, age)
VALUES 
    ("Test Dog", "PITTIE!!", 3) , 
    ("Test Dog2", "Golden Retriever", 7) ,
    ("Test Dog3", "Former U.S. President", 78);

# Note that somewhat confusingly vis-a-vis Python and understandably vis-a-vis R, SQL doesn't care about newlines, spaces or tabs.
# So, I can go back to formatting things to look nice like I did in R.

INSERT INTO dogs (name) VALUE ("NullDog");

# Avoid NULL with NOT NULL!

Create Table betterdogs
(
    name varchar(100) NOT NULL,
    bred varchar(100) NOT NULL,
    age INT NOT NULL
);

INSERT INTO betterdogs (name) VALUE ("NullDog");
# Error Code: 1364. Field 'bred' doesn't have a default value
# NullDog isn't added

# Whoops, I should always use single quotes because double quotes don't work well with all types of relational databases

# How to insert a quote into a string? Escape it

insert into dogs (name) VALUE ("Fancy's Dog"); # Lmao whoops this worked because I used different types of quotes, but I'm not supposed to use double quotes so let's try it again

insert into dogs (name) VALUE ('Even_Fancier\'s Dog');
# That also worked, but this should not:

# insert into dogs (name) VALUE ('Fanciest's Dog;');
# # Yep, it doesn't work.' I'm commenting out that code so Workbench gets off my back, but uncomment it to see.

# Setting Default Values

ALTER TABLE dogs ALTER breed SET DEFAULT 'Mixed', ALTER name SET DEFAULT 'Unknown', ALTER age SET DEFAULT 99;

# What happens if you try to set a string column to datatype INT?

ALTER TABLE dogs MODIFY breed INT;
# It doesn't let you.
# Error Code: 1366. Incorrect integer value: 'Pomewawa' for column 'breed' at row 1

# Adding a PRIMARY KEY to a table:

# Don't need to specify a primary key is NOT NULL because primary keys can never be NULL.
ALTER TABLE dogs ADD DogID int PRIMARY KEY AUTO_INCREMENT;

DESC dogs;

# Test creating a table

CREATE DATABASE employee;

CREATE TABLE employees 
( 
id INT PRIMARY KEY AUTO_INCREMENT,
last_name VARCHAR() NOT NULL,
first_name VARCHAR() NOT NULL,
middle_name VARCHAR(),
age INT NOT NULL,
current_status VARCHAR(), NOT NULL, SET DEFAULT 'employed'
);
# Doesn't work, you HAVE to set a length for VarChar

CREATE TABLE employees 
( 
id INT PRIMARY KEY AUTO_INCREMENT,
last_name VARCHAR(255) NOT NULL,
first_name VARCHAR(255) NOT NULL,
middle_name VARCHAR(255),
age INT NOT NULL,
current_status VARCHAR(255) NOT NULL DEFAULT 'employed'
);
# TAKE HEED - it is "SET DEFAULT" in ALTER TABLE but just DEFAULT in CREATE TABLE!

desc employees;

