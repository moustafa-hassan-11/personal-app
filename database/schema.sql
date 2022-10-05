create database restaurant;

use restaurant;

create table users (userID int NOT NULL UNIQUE AUTO_INCREMENT,username VARCHAR(30) NOT NULL UNIQUE, fn VARCHAR(40) NOT NULL ,ln VARCHAR(40) NOT NULL,age int NOT NULL,gender VARCHAR(10) NOT NULL,password VARCHAR(40) NOT NULL,PRIMARY KEY(userID));

create table rest (restID int NOT NULL UNIQUE AUTO_INCREMENT,rest_name VARCHAR(40) NOT NULL,food_type VARCHAR(20) NOT NULL,review VARCHAR(20) NOT NULL,PRIMARY KEY(restID));

create table orders (orderID int NOT NULL UNIQUE AUTO_INCREMENT,order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,items VARCHAR(500) NOT NULL,userID int NOT NULL,restID int NOT NULL,FOREIGN KEY (userID) REFERENCES users(userID),FOREIGN KEY (restID) REFERENCES rest(restID),PRIMARY KEY(orderID));

create table management (mesgID int NOT NULL UNIQUE AUTO_INCREMENT,message VARCHAR(40) NOT NULL);

create view order_view AS  select orders.order_date, users.username, orders.items, rest.rest_name from orders, users, rest where orders.restID = rest.restID and orders.userID = users.userID;

insert into management (message) values ("echo from database");

INSERT INTO users (username,fn,ln,age,gender,password) values ("admin","admin","admin",28,"male","admin@123");

insert into rest (rest_name,food_type,review) values ('StarBucks','Beverages','amazing');

insert into rest (rest_name,food_type,review) values ('SaleSucree','Deserts','Good');


CREATE USER   rest@'%' IDENTIFIED BY 'root123';

GRANT all ON restaurant.* TO rest@'%';

FLUSH PRIVILEGES ;
