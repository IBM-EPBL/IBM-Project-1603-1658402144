import time
from random import randint
file=open("data.txt","a")
n=5
for i in range(n):
    humidity=randint(0,100)+1
    temperature=randint(-100,100)+1
    if humidity>45:
        print("\n \n Humidity High")
        print(humidity)

        file.write("\nHumidity")
        file.write(str(humidity))

    if temperature>30:
        print("Temperature High")
        print( temperature)

        file.write("\nTemperature")
        file.write(str(temperature))
    time.sleep(1)
file.close()

Program 2:
t=int(input("Enter the Temperature:")) #Temperature

h=int(input("Enter the Humidity:")) #Humidity

while(t>35):

      print("Buzzer ON")
