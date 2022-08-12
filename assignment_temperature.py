# Program: [Your Initials]_7dayThermometer.py
# Date: 8-Jun-2022
# Author: [Your Name] (Student #[Your Student Number])
# Description: The program reads the temp in celsius of a week and displays the temp in Fahrenhite along with max,min and totaltemp of the week 
weeks=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
tempCelsius=[]
tempFahrenhite = []
maxTemp =0.0
minTemp =0.0
totalTemp =0.0
for i in range(0,7):
    x=float(input("Please enter the temperature for " + weeks[i] + " in Celsius: "))
    tempCelsius.append(x)
    y = round((x * 1.8) + 32,2)
    tempFahrenhite.append(y)

#finding max and min temp
minTemp = tempCelsius[0]
for i in range(0,7):
    if maxTemp < tempCelsius[i]:
        maxTemp=tempCelsius[i]
    if minTemp > tempCelsius[i]:
        minTemp = tempCelsius[i]
    totalTemp += tempCelsius[i]


        
#bubble sort
for i in range(0,7):
    for j in range(0,7-i-1):
        if tempCelsius[j] > tempCelsius[j+1]:
            tempCelsius[j],tempCelsius[j+1] =tempCelsius[j+1],tempCelsius[j] 

#displaying the data
print("\nYou entered these Temperatures in Celsius and Fahrenheit.\n")
for i in range(0,7):
    print(str(tempCelsius[i])+" C° is " + str(tempFahrenhite[i])+" F° ")
print("-----------------")
avgTemp = round(totalTemp /7,1)
print("High Temp: " + str(maxTemp) + " C°, Low Temp: " + str(minTemp) + " C° and Average Temp: " + str(avgTemp) + " C°")
