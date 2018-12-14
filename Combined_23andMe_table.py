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
    db='23andMe_Collective_Table')
cursor = mydb.cursor()

# this is how I created the SQL TABLE
# CREATE TABLE HU0DEE68(rsid varchar(20) not null, chromosome varchar(5) not null,
# position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));

# this opens the 23andMe file
file = open("hu0DEE68.txt", "r")
# this breaks up into individual lines
lines = file.readlines()

# this for loop cycles through all of the lines
for line in lines:
    # this splits up each line into individual words
    columns = line.split()
    # the first ~29 lines of a 23andMe file are # comments that aren't useful
    # the if jumps over lines that start with #
    if columns[0] == "#":
        continue
    # these lines have the data
    else:
        # this part of the 23andMe file has four columns
        # column 1 is rsid, column 2 is chromosome, column 3 is position,
        # and column 4 is genotype
        rsid = columns[0]
        chromosome = columns[1]
        position = columns[2]
        genotype = columns[3]

        # PERCENT STRING FORMATTING
        #print("""INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype))
        # here's the command
        #command = """INSERT INTO HU0DEE68 (rsid, chromosome, position, genotype) VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype)
        # this executes the MySQL command
        #cursor.execute(command)
        print("""INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES({rsid}, {chromosome}, {position}, {genotype});""".format(rsid=rsid, chromosome=chromosome, position=position, genotype=genotype))
        command = """INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES('{rsid}', '{chromosome}', '{position}', '{genotype}');""".format(rsid=rsid, chromosome=chromosome, position=position, genotype=genotype)
        cursor.execute(command)
file.close()
mydb.commit()
cursor.close()
