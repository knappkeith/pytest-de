Create a Database:

```sql
CREATE DATABASE [DB_Name];

SHOW databases;

USE [DB_Name];
```

##Create a Table:
---

### USERS TABLE:
Create Table:
```sql
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    ip_address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
)  ENGINE=INNODB;
```
Populate:
```sql
LOAD DATA LOCAL INFILE '/Users/keith.knapp/dev/pytest-de/assets/MOCK_DATA_user_landing.csv'  INTO TABLE users
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```


### ADDR TABLE
Create Table:
```sql
CREATE TABLE IF NOT EXISTS addr (
    id INT AUTO_INCREMENT,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    state VARCHAR(255) NOT NULL,
    zip_code VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
)  ENGINE=INNODB;
```
Populate:
```sql
LOAD DATA LOCAL INFILE '/Users/keith.knapp/dev/pytest-de/assets/MOCK_DATA_addr_landing.csv'  INTO TABLE addr
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```

### ORDERS TABLE:
Create Table:
```sql
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT,
    quanity INT NOT NULL,
    sku VARCHAR(255) NOT NULL,
    order_total DECIMAL(5,2) NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (id)
)  ENGINE=INNODB;
```
Populate:
```sql
LOAD DATA LOCAL INFILE '/Users/keith.knapp/dev/pytest-de/assets/MOCK_DATA_orders.csv'  INTO TABLE orders
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```


If you get error `Error Code: 3948. Loading local data is disabled; this must be enabled on both the client and server sides` from `LOAD DATA LOCAL` Command:

```sql
SET GLOBAL local_infile=1;
```




to start and stop mysql from command line

```bash
# START
$ sudo launchctl load -F /Library/LaunchDaemons/com.oracle.oss.mysql.mysqld.plist

# STOP
$ sudo launchctl unload -F /Library/LaunchDaemons/com.oracle.oss.mysql.mysqld.plist
```
