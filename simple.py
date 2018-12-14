#!/usr/bin/python

# the goal of this code is to automate the SQL insertion commands
# for hundreds of 23andMe files being inserted into MySQL

# this module is used for interacting with a MySQL database
import MySQLdb

# I pulled some of the starter code for connecting to a MySQL database from StackOverflow
# insert into mysql table using python from text file
# this was inspired by https://stackoverflow.com/questions/45334619/insert-into-mysql-table-using-python-from-text-file

# this connects to my database
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='elfcheese',
    db='23andMe')
cursor = mydb.cursor()

# this works, so what's wrong with the above?
test = """INSERT INTO HU0DEE68 (rsid, chromosome, position, genotype) VALUES("rs1554480", "3", "233424", "AA")"""
cursor.execute(test)

# this is how I created the SQL TABLE
# CREATE TABLE HU0DEE68(rsid varchar(20) not null, chromosome varchar(5) not null,
# position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));

mydb.commit()
cursor.close()
