#!/usr/bin/python

# add all 23andMe files to one MySQL Table

# this cycles through all the ACTUAL 23andMe files (382)
#############################################################
import os
list = os.listdir("/media/david/Terabyte/2018-06-13_DOWNLOAD_PGP")
twentythree_counter = 0
for file in list:
    full_path = "/media/david/Terabyte/2018-06-13_DOWNLOAD_PGP/" + file
    file_data = open(full_path, "r")
    lines = file_data.readlines()

    if "23andMe" not in lines[0]:
        continue
    else:
        print file
        twentythree_counter += 1
print "twenty three and me files counter is: "
print twentythree_counter
############################################################
