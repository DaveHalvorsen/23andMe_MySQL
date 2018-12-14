#!/usr/bin/python


import MySQLdb
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='elfcheese',
    db='23andMe')
cursor = mydb.cursor()


filename = "hu1AF744.txt"
file_text = filename.split('.')
table_name = file_text[0]
print (file_text[0])

cursor.execute("""CREATE TABLE {table_name}(rsid varchar(20) not null, chromosome varchar(5) not null, position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));""".format(table_name=table_name))
