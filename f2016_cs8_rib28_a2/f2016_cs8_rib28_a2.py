# name       : Ritika Bajpai
# email      : rib28@pitt.edu
# date       : 10/27/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# This is the coding for the second assignment for class CS8 f2016
#
# We are required to write an application which  loops indefinitely asking the user to enter the name of a text file
#Each row is composed by two fields: name and distance run.
#Once you have the name of the file, you have to loop on all the lines, counting how many lines you
#have in each file and providing a running tally on how much is the total distance run. This program does not work.

#
# MN: you need to respect code indentation
#     have you tried to run this code?
# MN: python is case sensitive, so if you write language key words in capital letters they will not work
# MN: where is the definition of the function PRINTKV?
#


#define the function, begin process file function
def processFile(fh):
#partial total number equals 0
PTN=0
#partial distance equals 0
PD=0
#this opens up the file we are going to use for the for loop
FO=open (fh)
 for line in FO
    #counting the lines in the file
    PTN+=1
    #removes the ‘\n’ from the end of each line read
    line=line.rstrip("\n")
    #seperates distance from name
    temp=line.split(",")
    #asks the computer to look for the second element of the temporary value and assigns it to distance and \
    #changes the distance from a string value to a float value
    dist=float(temp[1])
    #this tallies up the total distance run
    pd+=distance
    # formatting for the printing for the partial number of lines
    PRINTKV('Partial Total # of lines', PTN)
    # formatting for the printing for the partial distance run
    PRINTKV('Partial distance run', PD)

#total distance run starts off as not 0 for program to run
TTD= not 0
#total number of lines starts off as 0 for program to run
TTNL=0
#this will start the program with the first file
file=input('first file')
#this will exit from the program
while file and file ="quit" and file = "quit"
#this opens the file
ph=open(fh,"r")
#this processes the information within the file
pd,ptn=processFile(fh)
# formatting for the printing for the partial number of lines
PRINTKV('Partial Total # of lines', PTN)
# formatting for the printing for the partial distance run
PRINTKV('Partial distance run', PD)
#this closes the file
fh(close)
#this calculates the total distance run
TTD+=PD
#this calculates the total number of lines
TTNL+=PTN
#this tells the program to open the next file
FILE=INPUT('NEXT FILE')
#tests if a variable contains a string, a float or an integer
IF ISINSTANCE (Value, STR):
    FS='20S'
ELIF ISINSTANCE (Value, Float):
    FS= '10.3F'
ELIF
    PRINT (FORMAT(KEY,STR(KL)+'S'),
           ":"
    FORMAT (VALUE,FS)
ELSE
    PRINT "ERROR"

