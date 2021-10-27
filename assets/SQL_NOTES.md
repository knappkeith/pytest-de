Create a Database:

```sql
CREATE DATABASE [DB_Name];

SHOW databases;

USE [DB_Name];
```

Create a Table:

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

Load data into table from csv:

```sql
LOAD DATA LOCAL INFILE '/Users/keith.knapp/Downloads/MOCK_DATA.csv'  INTO TABLE users
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