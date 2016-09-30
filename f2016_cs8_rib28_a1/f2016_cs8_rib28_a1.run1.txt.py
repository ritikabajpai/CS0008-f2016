#created a function for consumption rating which will work for USC and Metric system
def consumptionRating(consumption):
#setting parameters for the different outputs to be used for the consumption rating
	if(consumption>20):
		print(" Gas Consumption Rating:Extremely Poor")
	elif(consumption<=20 and consumption>15):
		print("Gas Consumption Rating:Poor")
	elif(consumption<=15 and consumption>10):
		print("Gas Consumption Rating:Average")
	elif(consumption<=10 and consumption>8):
		print("Gas Consumption Rating:Good")
	else:
		print("Gas Consumption Rating:Excellent")
#prompt user to choose a program
print("Choose a system")
#user provides input about system by choosing a number that has to be an integer
system=int(raw_input("Press 1 for USC and 2 for Metric: "))
#creating a variable for distance driven
distancedr=float(raw_input("How far did you drive: "))
#creating a variable for gas used
gasused=float(raw_input("How much gas did you use: "))
if(system==1): #when user chooses USC system
	#calculate distance fron miles to kilometers
	distancem=distancedr*1.60934
	#calculate gas used from gallons to liters
	gasm=gasused*3.78541
	#calculate miles per gallon for consumption
	mpg=distancedr/gasused
	#calculate liters per kilometer for consumption
	lpkm=100*gasm/distancem
    #printing the distance and also changing the distance from intergers to strings to prevent logic errors
	print("Distance: " +str(distancedr) +" miles " +str(distancem)+" Km")
    #printing the gas and also changing the gas usuage values from intergers to strings to prevent logic errors
	print("Gas: " +str(gasused) + " gallons " +str(gasm)+ "liters")
    #printing the consumption and also changing the gas consumption values from intergers to strings to prevent logic
    # errors
	print("Consumption " +str(mpg)+" miles per gallon " +str(lpkm)+" l/100 km ")
    #putting the function for consumption ratings into effect
	consumptionRating(lpkm)
if(system==2): #when user chooses metric system
	#calculate distance from kilometers to miles
	distanceu=distancedr*0.621371
	#calculate gas used from liters to gallons
	gasu=gasused*0.264172
	#calculate miles per gallon for consumption
	mpg2=distanceu/gasu
	#calculate liters per kilometer for consumption
	lpku=100*distancedr/gasused
    #printing the distance and also changing the distance from intergers to strings to prevent logic errors
	print("Distance: " +str(distanceu) +" miles " +str(distancedr)+" Km")
    #printing the gas and also changing the gas usuage values from intergers to strings to prevent logic errors
	print("Gas: " +str(gasu) + " gallons " +str(gasused)+ "liters")
    #printing the consumption and also changing the gas consumption values from intergers to strings to prevent logic
    # errors
	print("Consumption " +str(mpg2)+" miles per gallon " +str(lpku)+" l/100 km ")
    #putting the function for consumption ratings into effect
	consumptionRating(lpku)
