#!/usr/bin/python

# add all 23andMe files to one MySQL Table

# this module is used for interacting with a MySQL database
import MySQLdb
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='password',
    db='23andMe_Collective_Table')
cursor = mydb.cursor()




# this cycles through all the ACTUAL 23andMe files (382)
import os
list = os.listdir("/media/david/Terabyte/2018-06-13_DOWNLOAD_PGP")
file_counter = 0
for file in list:
    # several errors crashed the program, so this let me restart things
    # note that the last table had to get dropped before it'd run
    #if file_counter <= 389:
        #file_counter += 1
        #continue
    full_path = "/media/david/Terabyte/2018-06-13_DOWNLOAD_PGP/" + file
    file_data = open(full_path, "r")
    lines = file_data.readlines()
    # only use 23andMe data files (there's GoodforGenes, Ancestry & Promoethease files)
    if "23andMe" not in lines[0]:
        file_counter += 1
        continue
    # get rid of 23andMe established research reports
    if "23andMe Established Research Reports" in lines[0]:
        file_counter += 1
        continue
    else:
        # print file
        #print file
        file_text = file.split('.')
        #print file_text[0]
        table_name = file_text[0]

        # only one table is required, so I'll enter it manually
        # MAKE SQL COMMAND FOR TABLE CREATION HERE
        # create SQL table for current file
        # cursor.execute("""CREATE TABLE 23andMe_Specimen_Table(rsid varchar(20) not null, chromosome varchar(5) not null, position varchar(20) not null, genotype varchar(2) not null, constraint pk_example primary key (rsid));""".format(table_name=table_name))
        #
        # open current file
        file = open(full_path, "r")
        # this breaks up into individual lines
        lines = file.readlines()

        # this for loop cycles through all of the lines
        # last_rsid is part of a feature that fixes a crash
        last_rsid = "I like to eat peanut butter"
        for line in lines:
            # this splits up each line into individual words
            columns = line.split()
            # blank line in file hu9122D5.txt
            if len(columns) != 4:
                continue
            if columns[0] == "":
                continue
            # the first ~29 lines of a 23andMe file are # comments that aren't useful
            # the if jumps over lines that start with #

            if columns[0] == "#":
                continue
            # this doesn't work ... I think line.split is the issue
            # hu9122D5 has a blank line in it's 23andMe listing
            #if columns[0] == "":
                #continue
            # these lines have the data
            else:
                # this part of the 23andMe file has four columns
                # column 1 is rsid, column 2 is chromosome, column 3 is position,
                # and column 4 is genotype
                rsid = columns[0]
                chromosome = columns[1]
                position = columns[2]
                genotype = columns[3]

                # huDA4FBE.txt has two entries for rs150666616
                # it will cause an integrity error if you try to overwrite
                # (Error 1062 Duplicate Key)
                if rsid == last_rsid:
                    continue

                # old way
                #print("""INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES({rsid}, {chromosome}, {position}, {genotype});""".format(rsid=rsid, chromosome=chromosome, position=position, genotype=genotype))
                #command = """INSERT INTO HU0DEE68(rsid, chromosome, position, genotype) VALUES('{rsid}', '{chromosome}', '{position}', '{genotype}');""".format(rsid=rsid, chromosome=chromosome, position=position, genotype=genotype)
                print "current file is: " + str(file_counter)
                print("""INSERT INTO {table_name}(rsid, chromosome, position, genotype) VALUES('{rsid}', '{chromosome}', '{position}', '{genotype}');""".format(table_name=table_name, rsid=rsid, chromosome=chromosome, position=position, genotype=genotype))
                cursor.execute("""INSERT INTO {table_name}(rsid, chromosome, position, genotype) VALUES('{rsid}', '{chromosome}', '{position}', '{genotype}');""".format(table_name=table_name, rsid=rsid, chromosome=chromosome, position=position, genotype=genotype))


                # this'll be the last rsid on the next loop cycle
                last_rsid = rsid
        file.close()
        file_counter += 1

mydb.commit()
cursor.close()
