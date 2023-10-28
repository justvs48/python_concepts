
from playsound import playsound
import time
def alarm(minutes):
    i=1
    print("ticking...")
    while True:
        
        time.sleep(1)
        print(".")
        
        
        i+=1
        if i==(minutes*60):
            print("2 minute passed")
            for j in range(10):
                playsound("C:\\Users\\saizal\\Downloads\\beep.wav")
                
            break
minutes=float(input("enter the alarm time in minutes (ie 2 mean 2 minutes) :  "))
alarm(minutes)
        


