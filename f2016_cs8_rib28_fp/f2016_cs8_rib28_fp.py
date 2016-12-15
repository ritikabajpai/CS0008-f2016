# name       : Ritika Bajpai
# email      : rib28@pitt.edu
# date       : 12/14/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# This is the coding for the final assignment for class CS8 f2016
# Write a program that read the master input list file, retrieves the names of the data files and from each
#one of the data files reads every line, extract name and distance. Once the program has all the data in
#memory, it has to compute the following quantities and informations:
#number of files read in input
#total number of lines read
#  total distance run (aka the sum of all the distances loaded from provided files)
#total distance run for each individual participant
#individual maximum distance run and by which participant
#individual minimum distance run and by which participant
#report if there are any participants that appears more than once, how many times and their names
#total number of participants


# we define class participant definition according to the instructions
class participant:
    """participant class """
#participant name
    name = "unknown"
#distance run by participant
    distance = 0
#number of runs by participant
    runs = 0

 #initializer methods
    def __init__(self, name, distance=0):
        self.name = name
        if distance > 0:
            self.distance = distance
            self.runs = 1
#get the name of the participants from the file
    def getname(self):
        return self.name
#get the distance variable for the accumulator
    def getDistance(self):
        return self.distance
#adds the distances run for the runners who ran more than once
    def getRuns(self):
        return self.runs
#setting up the distance accumulator for people who ran once
    def addDistance(self, distance):
        if distance > 0:
            self.distance += distance
            self.runs += 1
#setting up the distance accumulator for runners who ran more than once,
# like addDistance we are adding the variables of distances set up to our distance accumulator
    def addDistances(self, distances):
        for distance in distances:
            if distance > 0:
                self.distance += distance
                self.runs += 1
#returning a string with our name,distance ran and how much distance was run
# and runners who ran more were present
    def __str__(self):
        return \
#right aligning our string and setting a limit of20 characters
#for our name, a limit of 9 digits for total distance and 4 digits for the number of
#ones
        "Name : " + format(self.name, '>20s') + \
        ". Distance run : " + format(self.distance, '9.4f') + \
        ". Runs : " + format(self.runs, '4d')
# converting our data to the correct excel format
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])
#extracting the data from our excel document
    def getDataFromFile(file):
        output = []
        for line in open(file, 'r'):
            if "distance" in line:
                continue
#removing the newline character and spliting the two columns of our excel documents
            temp1 = line.rstrip('\n').split(',')
            try:
                output.append({'name': temp1[0].strip(' '), 'distance': float(temp1[1])})
            except:
                 print('Invalid row : ' + line.rstrip('\n'))
            return output
#formatting of the information from the files
    def printKV(key, value, klen):
        key_length = len(key)
        if klen > key_length:
            key_length = klen

        key = format(key, str(key_length)+'s')
        if isinstance(value, str) == True:
             value = format(value, '.20s')

        elif isinstance(value, float) == True:
          value = format(value, '12.5f')
          value = format(str(value), '.30s')

        else:
           value = format(value, '5d')
           value = format(str(value), '.30s')

        print(key+' : '+value)

    def main():
    #begin loop
        masterFile = input("Please provide master file : ")
        try:
             dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
        except:
            print("Impossible to read master file or invalid file name")
            exit (1)

        exceldata = sum([getDataFromFile(file) for file in dataFiles],[])
        numberFiles = len(dataFiles)
#he variable for the total lines and distance that will be displayed when the user quits the program
        totalline = len(exceldata)
        totaldistanceRun = sum([item['distance'] for item in exceldata])
        participants = {}
 # Finding if any name has already been read
        for item in exceldata:
            if not item['name'] in participants.keys():
               participants[item['name']] = participant(item['name'])
            participants[item['name']].addDistance(item['distance'])

# setting up the minimum and maximum intervals for our dictionaries

            minDistance = {'name': None, 'distance': None}
            maxDistance = {'name': None, 'distance': None}
            partcipation = {}
#Finding the actual minimum and maximum distance for our dictionary
#Finding and setting the new minimum and maximum for our dictionary when they are read
        for name, object in participants.items():
            distance = object.getDistance()
            if minDistance['name'] is None or minDistance['distance'] > distance:
                minDistance['name'] = name
                minDistance['distance'] = distance

            if maxDistance['name'] is None or maxDistance['distance'] < distance:
                maxDistance['name'] = name
                maxDistance['distance'] = distance

            participantAppearences = object.getRuns()
            if not participantAppearences in partcipation.keys():
                participation[participantAppearences] = []
            participation[participantAppearences].append(name)
#The length of the participants in the dictionary will give us the number of participants
         totalparticipants = len(participants);
# we compute total number of participants with more than one record
# extract all the participants that have 2 or more runs
# and count the number of elements in the list with len()
        totalmultiplerecordholders = len([1 for item in participants.values() if item.getRuns() > 1])
        INTEGER = '5d'
        FLOAT = '12.5f'
        STRING = '20s'
#printing the output
        printKV('Number of Input files read', numberFiles, 28)
        printKV('Total number of lines read', totalline, 28)
        print('')
        printKV('Total distance run', totaldistanceRun, 28)
        print('')
        printKV('Max distance run', maxDistance['distance'], 28)
        printKV('   by participant', maxDistance['name'], 28)
        print('')
        printKV('Min distance run', minDistance['distance'], 28)
        printKV('   by participant', minDistance['name'], 28)
        print('')
        printKV('Total number of participants', totalparticipants, 28)
        print('Number of participants')
        printKV('   with multiple records', totalmultiplerecordholders, 28)
        print('')
#we are converting the data that we read and displayed from our excel documents and creating the output file required
# according to the instructions
        outputFile = "f2016_cs8_rib28_fp.output.csv"
        fh = open(outputFile,'w')
        fh.write('name,records,distance\n')
        for name, object in participants.items():
             fh.write(object.tocsv() + '\n')
#we have to close the file to make sure there are no errors
        fh.close()

main()