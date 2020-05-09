distance = 0
time = 60
speed = 0
points = 1
limiteddistance = 5
demeritpoints = 0

distance = int(input("Enter the distance you have covered in (Kms): "))
time = int(input("Enter the time you have covered in (hrs): "))

def calculate_Speed(speed,demeritpoints):
      speed = distance/time
      print("Your speed is: "+str(speed)+ " Km/hr")
      if (distance <= limiteddistance)and (speed < 70):
            print("Its Ok")

      elif (distance <= limiteddistance and speed >= 70):
            demeritpoints = demeritpoints + 1
            print("Your points collected are: "+str(demeritpoints)) 

      elif (distance == limiteddistance) and (speed == 80):
            demeritpoints = demeritpoints + 2
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 90):
            demeritpoints = demeritpoints + 3
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 100):
            demeritpoints = demeritpoints + 4
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 110):
            demeritpoints = demeritpoints + 5
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 120):
            demeritpoints = demeritpoints + 6
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 130):
            demeritpoints = demeritpoints + 7
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 140):
            demeritpoints = demeritpoints + 8
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 150):
            demeritpoints = demeritpoints + 9
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 160):
            demeritpoints = demeritpoints + 10
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 170):
            demeritpoints = demeritpoints + 11
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 180):
            demeritpoints = demeritpoints + 12
            print("Your points collected are: "+str(demeritpoints))

      elif (distance == limiteddistance) and (speed == 190):
            demeritpoints +=  13
            print("Your points collected are: "+str(demeritpoints))
      else:
            print("You have no demerit points")


      if (demeritpoints < 12):
            print("Continue")
      else:
            print(" License suspended")
            

      return demeritpoints
      return speed

     
      

calculate_Speed(speed,demeritpoints)





    
