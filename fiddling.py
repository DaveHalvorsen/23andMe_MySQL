#!/usr/bin/python
import MySQLdb
# this was inspired by https://stackoverflow.com/questions/45334619/insert-into-mysql-table-using-python-from-text-file

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='23andMe')
cursor = mydb.cursor()

#rsid = "RSIDZ"
#chromosome = "crhOMIES"
#position = "pos"
#genotype = "g-UNIT"
#test = """INSERT INTO HU0DEE68 (rsid, chromosome, position, genotype) VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype)

# this works, so what's wrong with the above?
#test = """INSERT INTO HU0DEE68 (rsid, chromosome, position, genotype) VALUES("rs15480", "3", "233424", "AA")"""
#cursor.execute(test)

file = open("hu0DEE68.txt", "r")
# print file.read()
lines = file.readlines()
# print(lines[15])S

for line in lines:
    columns = line.split()
    # print(columns[0])
    if columns[0] == "#":
        continue
    else:
        rsid = columns[0]
        chromosome = columns[1]
        position = columns[2]
        genotype = columns[3]
        # print("""INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype))
        command = """INSERT INTO HU0DEE68 (rsid, chromosome, position, genotype) VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype)
        print (command)
        # print("""INSERT INTO HU0DEE68 VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype))
        # cursor.execute("""INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype))
        #cursor.execute("""INSERT INTO HU0DEE68 VALUES(%s, %s, %s, %s);""" % (rsid, chromosome, position, genotype))
        cursor.execute(command)

#print(values[1])

# values = lines.split()
# print(values)


# INSERT INTO TABLE (rsid, chromosome, position, genotype) VALUES (%s, %s, %s, %s)

file.close()
mydb.commit()
cursor.close()

# CREATE TABLE HU0DEE68(rsid varchar(20) not null, chromosome varchar(5) not null, position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));
