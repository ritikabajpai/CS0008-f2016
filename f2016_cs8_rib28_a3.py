# name       : Ritika Bajpai
# email      : rib28@pitt.edu
# date       : 11/18/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# This is the coding for the third assignment for class CS8 f2016
# Write a program that read the master input list file, retrieves the names of the data files and from each
#one of them reads every line, extract name and distance. Once the program has all the data in memory,
#it has to compute the following quantities and informations:
#• number of files read in input
#• total number of lines read
#• total distance run (aka the sum of all the distances loaded from provided files)
#• total distance run for each individual participant
#• individual maximum distance run and by which participant
#• individual minimum distance run and by which participant
#• report if there are any participants that appears more than once, how many times and their names
#• total number of participants
#The program should provide an terminal output similar to the following:
#Number of Input files read : xx
#Total number of lines read : xx
#total distance run : xxxx.xxxxx
#max distance run : xxxx.xxxxx by participant : participant name
filename=”words”
fh=open(filename,’r’)
words=fh.readlines()
fh.close()
for line in words:
	line.rstrip(‘\n’)
Words_no_duplicates = list(set(words3))
words_no_duplicates.sort()
