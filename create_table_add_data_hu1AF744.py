#!/usr/bin/python

# the ultimate goal is to automate the SQL insertion commands
# for hundreds of 23andMe files being inserted into MySQL
# I'm not there yet. This code adds the entirety of
# the 23andMe file hu0DEE68.txt to the already
# established HU0DEE68 table.

# this module is used for interacting with a MySQL database
import MySQLdb
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='elfcheese',
    db='23andMe')
cursor = mydb.cursor()

# file to open
file_name = "hu1AF744.txt"


file_text = file_name.split('.')
table_name = file_text[0]
print table_name


# this is how I created the SQL TABLE
# CREATE TABLE HU0DEE68(rsid varchar(20) not null, chromosome varchar(5) not null,
# position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));
# example table creation code
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
cursor.execute("""CREATE TABLE {table_name}(rsid varchar(20) not null, chromosome varchar(5) not null, position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));""".format(table_name=table_name))

#CREATE TABLE {table_name}(rsid varchar(20) not null, chromosome varchar(5) not null, position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));
# this opens the 23andMe file
file = open(file_name, "r")
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

        # old way
        #print("""INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES({rsid}, {chromosome}, {position}, {genotype});""".format(rsid=rsid, chromosome=chromosome, position=position, genotype=genotype))
        #command = """INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES('{rsid}', '{chromosome}', '{position}', '{genotype}');""".format(rsid=rsid, chromosome=chromosome, position=position, genotype=genotype)

        print("""INSERT INTO {table_name}(rsid, chromosome, position, genotype) VALUES('{rsid}', '{chromosome}', '{position}', '{genotype}');""".format(table_name=table_name, rsid=rsid, chromosome=chromosome, position=position, genotype=genotype))
        cursor.execute("""INSERT INTO {table_name}(rsid, chromosome, position, genotype) VALUES('{rsid}', '{chromosome}', '{position}', '{genotype}');""".format(table_name=table_name, rsid=rsid, chromosome=chromosome, position=position, genotype=genotype))


        #cursor.execute(command)
file.close()
mydb.commit()
cursor.close()
