#-------------------#
#Greenfly Simulation#
#By Michael Peacock #
#10/11/15 - 12/01/16#
#-------------------#
import shutil
from random import randint
valuePASenior = 20
valuePAAdult = 20
valuePAJuv = 20
valuePA = 60
valueSA = 0.75
valueBR = 2
valueAG = 25
valueDT = 5000
gen = 0
diseasefactor = 1.0
Ran = "False"

def menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran):
	print ("""-------------------------
1.	View Values
2.	Quit
3.	Run Model
4.	Export Data
5.	Set Generation Values
-------------------------""")
	#main menu. After selecting a option (except 2) you will return here
	Userinput = input ("Select A Option 1-5 : ")
	
	if Userinput == ("1"):
		print ("""-------------------------
Population Ammount: 
	Seniors""",valuePASenior,"""
	Adult""",valuePAAdult,"""
	Juviniles""",valuePAJuv,"""
	Total""",valuePA,"""
Survival Ammount:""",valueSA,"""
Birth Rate:""",valueBR,"""
Generations 5-25:""",valueAG,"""
Disease Trigger Point:""",valueDT,"""
-------------------------""")
		#Displays all values of the saved varables
		menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
		
	elif Userinput == ("2"):
		print ("Quitting")
		
	elif Userinput == ("3"):
		gen = -1
		while gen < valueAG:
			print ("""-------[Generation:""",gen+1,"""/""",valueAG,"""]-------
Population: 
    Seniors""",(round(valuePASenior)),"""
    Adult:""",(round(valuePAAdult)),"""
    Juviniles:""",(round(valuePAJuv)),"""
    Total:""",(round(valuePA)),"""/""",valueDT,"""
Disease Effect:""",diseasefactor)
			#loops until gen is the same value as the ammount of generations
			valuePASenior = valuePAAdult * valueSA 
			# sets seniors value to the ammount of adults * by the Survival ammount that will be lower than 1
			valuePAAdultold = valuePAAdult
			valuePAAdult = valuePAJuv * valueSA 
			# sets Adults value to the ammount of Juviniles * by the Survival ammount that will be lower than 1
			valuePAJuv = valuePAAdultold * valueBR * diseasefactor 
			# sets Juvinials value to the ammount of Seniors (that generations adults) * by the birthrate then * the disease factor
			valuePA = valuePAJuv + valuePAAdult + valuePASenior
			# sets the total value to all of Seniors, Adults and juviniles
			diseasefactor = 1.0
			if valuePA > valueDT:
				#checks if the total ammount of greenflys is higher than the disease trigger
				diseasefactor = randint(20, 50)
				#set the varable to a random number between 20 and 50
				diseasefactor = diseasefactor/100
				#divides the diseasefactor by 100
			gen = gen + 1
			#adds 1 to the total generations
			try:
				#using another csv should be more effecent than lists as it wont use ram to hold them
				Ran = "True"
				if gen == 0:
					#writes the headder of the file and clears the temp file
					TemporyFile=open("Tempfile.csv","w+") 
					TemporyFile.write("Generation,Seniors,Adults,Juvinils,Total Population,Survival Amount,Birth Rate,Disease Trigger,Disease Factor")
					TemporyFile.write("\n")
				#writes all the data from the program by appending the file
				TemporyFile=open("Tempfile.csv","a") 
				TemporyFile.write(str(gen))
				TemporyFile.write(",")
				TemporyFile.write(str(round(valuePASenior)))
				TemporyFile.write(",")
				TemporyFile.write(str(round(valuePAAdult)))
				TemporyFile.write(",")
				TemporyFile.write(str(round(valuePAJuv)))
				TemporyFile.write(",")
				TemporyFile.write(str(round(valuePA)))
				TemporyFile.write(",")
				TemporyFile.write(str(valueSA))
				TemporyFile.write(",")
				TemporyFile.write(str(valueBR))
				TemporyFile.write(",")
				TemporyFile.write(str(valueDT))
				TemporyFile.write(",")
				TemporyFile.write(str(diseasefactor))
				TemporyFile.write("\n")
				if gen == valueAG:
					TemporyFile.close()
			except IOError:
				print  ("Error Returned to menu - IOError Tempfile Open?")
				#if the file is open it will give a clear error
				gen = valueAG
				menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
			except OverflowError:
				print  ("Error Returned to menu - OverflowError Exceded Max Number?")
				#if the program excedes the max number it will stop running
				gen = valueAG
				menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
		else:
			print ("Finished and New Population Edited")
			gen = 0
			menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
			
	elif Userinput == ("4"):
		try:
			if Ran == "True":
				userinput = input ("File Name:")
				userinput = str.join('.', (userinput, 'csv'))
				FileExitsCheck=open(userinput,"r") #basic way to fix file saving
				Confirm = input ("This file exists!\nTo continue type '1' or '2' to quit\n")
				if Confirm == "1":
					shutil.move("tempfile.csv" , userinput)
					print ("File Saved!")
				else:
					print("Save Canceled")
					menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
			else:
				print ("Returned to menu. Run Model first")
				menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
		except FileNotFoundError:
				shutil.move("tempfile.csv" , userinput)
				print ("File Saved!")	
		except Exception:
				print  ("Error Returned to menu - Bad File Name?")
				#if the use uses ?/\():; in a file name it will stop
				gen = valueAG
				menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)	
	elif Userinput == ("5"):
		try:
			valuePASenior = int(input ("First generation of seniors: "))
			valuePAAdult = int(input ("First generation of adults: "))
			valuePAJuv = int(input ("First generation of juviniles:"))
			valueBR = float(input ("Birth Rate Min:0.1: "))
			valueSA = float(input ("Survival Rate Min:0.1: "))
			valueAG = int(input ("Amount of generations 5-25: "))
			valueDT = int(input ("Disease Trigger: "))
			menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
			#sets the values and returns to the menu
		except ValueError:
			print ("An error occured! returning to menu")
			menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
	else:
		menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
		
menu(gen,valuePASenior,valuePAAdult,valuePAJuv,valuePA,valueSA,valueBR,valueDT,valueAG,diseasefactor,Ran)
