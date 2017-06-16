import telnetlib
import time 

HOST = ("192.168.1.250")  
zone_ID = 1
zone_ID2 = 2
source1_ID = 1
source2_ID = 2
Sleep_Time = 10 
AmountOfTimes = 0
TNT = telnetlib.Telnet(HOST, 23, 5)

while True:
#for x in range(100)
    print('Zone 1')                
    TNT.read_until("Please Enter command:",5)
    time.sleep(Sleep_Time)
    TNT.write("OUT00" + str(zone_ID) + "FR00" + str(source2_ID) + "\n\n")

 
    
    print('Zone 2')
    TNT.read_until("Please Enter command:",5)
    time.sleep(Sleep_Time)
    TNT.write("OUT00" + str(zone_ID2) + "FR00" + str(source2_ID) + "\n\n")

    print('Zone 1')
    TNT.read_until("Please Enter command:",5)
    time.sleep(Sleep_Time)
    TNT.write("OUT00" + str(zone_ID) + "FR00" + str(source1_ID) + "\n\n")
  
    
    print('Zone 2')
    TNT.read_until("Please Enter command:",5)
    time.sleep(Sleep_Time)
    TNT.write("OUT00" + str(zone_ID2) + "FR00" + str(source1_ID) + "\n\n")
    
    

print("Done")  
TNT.close()  
#raw_input ("Press any Key to Quit: ")