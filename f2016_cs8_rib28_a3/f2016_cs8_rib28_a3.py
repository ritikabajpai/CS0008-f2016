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

# 
# MN: where is the rest of the program?
#     Suggestion: you should experiment and make lot's of errors!!!
#

#printing the output needed by the program
printKV('Number of Input files read', total_files, 28)
printKV('Total number of lines read', total_lines, 28)
print('')
printKV('total distance run', total_distance, 28)
print('')
printKV('max distance run', main_max[1], 28)
printKV(' by particpant', main_max[0], 28)
print('')
printKV('min distance run', main_min[1], 28)
printKV(' by participant', main_min[0], 28)
print('')
printKV('Total number of participants', len(main_dict), 28)
print('Number of participants')
printKV('with multiple records', len(main_appearances_dict), 28)

#creating the output file reporting name of the participant, how many times their
# name appears in the input files and the total distance run.
f = open('f2016_cs8_rib28_a3.data.output.csv', 'w')
f.close()

