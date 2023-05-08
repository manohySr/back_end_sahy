# Sahy is our team for a competition in our mention Telecommunication at ESPA
## Third place (Bronze) 
## back_end Sahy 
## It's the backend app of a facerecognition app, build with python/flask
## I did not make a dependencies file so:
### Install: facerecongition, flask
## How to run the project,
###   1) Use a sql database like: MySQL or postgreSQL
Here are the sql script for creating the database: 

              CREATE DATABASE sahy_database;
              USE sahy_database;

              CREATE TABLE person (
                  id INT PRIMARY KEY AUTO_INCREMENT,
                  last_name VARCHAR(255),
                  first_name VARCHAR(255),
                  address VARCHAR(255),
                  email VARCHAR(255),
                  birthday VARCHAR(10),
                  description VARCHAR(255),
                  photo_filename VARCHAR(255)
              );

###   2) clone the repository and install all the dependencies
###   3) for running => python main.py
