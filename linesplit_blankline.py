#!/usr/bin/python

file = "hu9122D5.txt"
full_path = "/media/david/Terabyte/2018-06-13_DOWNLOAD_PGP/" + file

file = open(full_path, "r")
# this breaks up into individual lines
lines = file.readlines()

# this for loop cycles through all of the lines
for line in lines:
    # this splits up each line into individual words
    columns = line.split()
    print columns
    print len(columns)
