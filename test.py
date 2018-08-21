
import time
import sensortag
import urllib
import subprocess
from subprocess import call
import os
import RPi.GPIO as GPIO

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
# set Trigger to HIGH
GPIO.output(GPIO_TRIGGER, True)

# set Trigger after 0.01ms to LOW
time.sleep(0.00001)
GPIO.output(GPIO_TRIGGER, False)

StartTime = time.time()
StopTime = time.time()

# save StartTime
while GPIO.input(GPIO_ECHO) == 0:
    StartTime = time.time()

# save time of arrival
while GPIO.input(GPIO_ECHO) == 1:
    StopTime = time.time()

# time difference between start and arrival
TimeElapsed = StopTime - StartTime
# multiply with the sonic speed (34300 cm/s)
# and divide by 2, because there and back
distance = (TimeElapsed * 34300) / 2

return distance
data1=0
data2=0
data3=0
etemp1,RHhumidity1,baromilli1,light1,bat1=9999,9999,9999,9999,9999
etemp2,RHhumidity2,baromilli2,light2,bat2=9999,9999,9999,9999,9999
etemp3,RHhumidity3,baromilli3,light3,bat3=9999,9999,9999,9999,9999
etemp4,RHhumidity4,baromilli4,light4,bat4=9999,9999,9999,9999,9999
etemp5,RHhumidity5,baromilli5,light5,bat5=9999,9999,9999,9999,9999
etemp6,RHhumidity6,baromilli6,light6,bat6=9999,9999,9999,9999,9999
etemp7,RHhumidity7,baromilli7,light7,bat7=9999,9999,9999,9999,9999
etemp8,RHhumidity8,baromilli8,light8,bat8=9999,9999,9999,9999,9999

time.sleep(1.0)

while True:

try:
    
    tag1 = sensortag.SensorTag('54:6c:0e:53:04:ef')
    tag1.IRtemperature.enable()
    tag1.humidity.enable()
    tag1.barometer.enable()
    tag1.lightmeter.enable()
    tag1.battery.enable()
    etemp1, targettemp1 = tag1.IRtemperature.read()
    etemp1, RHhumidity1 = tag1.humidity.read()
    etemp1, baromilli1 = tag1.barometer.read()
    bat1=tag1.battery.read()
    print "the battey level is"
    print bat1
    tag1.disconnect()
    del tag1
    print "OK sensor1 temp,humid,pressure"
    cmd = 'sensortag 54:6c:0e:53:04:ef -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light1= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor1 light sensor"
    print light1
    print "\n"

except Exception:
    print "Something wrong in Sensortag1"

try:
    
    tag2 = sensortag.SensorTag('54:6c:0e:53:01:11')
    tag2.IRtemperature.enable()
    tag2.humidity.enable()
    tag2.barometer.enable()
    tag2.lightmeter.enable()
    tag2.battery.enable()
    etemp2, targettemp2 = tag2.IRtemperature.read()
    etemp2, RHhumidity2 = tag2.humidity.read()
    etemp2, baromilli2 = tag2.barometer.read()
    bat2=tag2.battery.read()
    tag2.disconnect()
    del tag2
    print "OK sensor2 temp,humid,pressure"
    cmd = 'sensortag 54:6c:0e:53:01:11 -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light2= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor2 light sensor"
    print light2
    print "\n"

except Exception:
    print "Something wrong in Sensortag2"


try:
    
    tag3 = sensortag.SensorTag('54:6c:0e:52:d0:f8')
    tag3.IRtemperature.enable()
    tag3.humidity.enable()
    tag3.barometer.enable()
    tag3.lightmeter.enable()
    tag3.battery.enable()
    etemp3, targettemp3 = tag3.IRtemperature.read()
    etemp3, RHhumidity3 = tag3.humidity.read()
    etemp3, baromilli3 = tag3.barometer.read()
    bat3=tag3.battery.read()
    tag3.disconnect()
    del tag3
    
    print "OK sensor3 temp,humid,pressure"    
    cmd = 'sensortag 54:6c:0e:52:d0:f8 -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light3= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor3 light sensor"
    print light3
    print "\n"

except Exception:
    print "Something wrong in Sensortag3"

try:
    
    tag4 = sensortag.SensorTag('54:6c:0e:52:d2:8f')
    tag4.IRtemperature.enable()
    tag4.humidity.enable()
    tag4.barometer.enable()
    tag4.lightmeter.enable()
    tag4.battery.enable()
    etemp4, targettemp4 = tag4.IRtemperature.read()
    etemp4, RHhumidity4 = tag4.humidity.read()
    etemp4, baromilli4 = tag4.barometer.read()
    bat4=tag4.battery.read()
    tag4.disconnect()
    del tag4
    print "OK sensor4 temp,humid,pressure"

    
    cmd = 'sensortag 54:6c:0e:52:d2:8f -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light4= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor4 light sensor"
    print light4
    print "\n"

except Exception:
    print "Something wrong in Sensortag4"



try:
    
    tag5 = sensortag.SensorTag('98:07:2d:40:9a:83')
    tag5.IRtemperature.enable()
    tag5.humidity.enable()
    tag5.barometer.enable()
    tag5.lightmeter.enable()
    tag5.battery.enable()
    etemp5, targettemp5 = tag5.IRtemperature.read()
    etemp5, RHhumidity5 = tag5.humidity.read()
    etemp5, baromilli5 = tag5.barometer.read()
    bat5=tag5.battery.read()
    tag5.disconnect()
    del tag5
    print "OK sensor5 temp,humid,pressure"

    
    cmd = 'sensortag 98:07:2d:40:9a:83 -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light5= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor5 light sensor"
    print light5
    print "\n"

except Exception:
    print "Something wrong in Sensortag5"    



try:
    
    tag6 = sensortag.SensorTag('98:07:2d:27:d4:83')
    tag6.IRtemperature.enable()
    tag6.humidity.enable()
    tag6.barometer.enable()
    tag6.lightmeter.enable()
    tag6.battery.enable()
    etemp6, targettemp6 = tag6.IRtemperature.read()
    etemp6, RHhumidity6 = tag6.humidity.read()
    etemp6, baromilli6 = tag6.barometer.read()
    bat6=tag6.battery.read()
    tag6.disconnect()
    del tag6
    print "OK sensor6 temp,humid,pressure"

    
    cmd = 'sensortag 98:07:2d:27:d4:83 -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light6= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor6 light sensor"
    print light6
    print "\n"

except Exception:
    print "Something wrong in Sensortag6"


try:
    
    tag7 = sensortag.SensorTag('98:07:2d:27:d7:03')
    tag7.IRtemperature.enable()
    tag7.humidity.enable()
    tag7.barometer.enable()
    tag7.lightmeter.enable()
    tag7.battery.enable()
    etemp7, targettemp7 = tag7.IRtemperature.read()
    etemp7, RHhumidity7 = tag7.humidity.read()
    etemp7, baromilli7 = tag7.barometer.read()
    bat7=tag7.battery.read()
    tag7.disconnect()
    del tag7
    print "OK sensor7 temp,humid,pressure"

    
    cmd = 'sensortag 98:07:2d:27:d7:03 -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light7= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor7 light sensor"
    print light7
    print "\n"

except Exception:
    print "Something wrong in Sensortag7"       



try:
    
    tag8 = sensortag.SensorTag('98:07:2d:40:bd:01')
    tag8.IRtemperature.enable()
    tag8.humidity.enable()
    tag8.barometer.enable()
    tag8.lightmeter.enable()
    tag8.battery.enable()
    etemp8, targettemp8 = tag8.IRtemperature.read()
    etemp8, RHhumidity8 = tag8.humidity.read()
    etemp8, baromilli8 = tag8.barometer.read()
    bat8=tag8.battery.read()
    tag8.disconnect()
    del tag8
    print "OK sensor8 temp,humid,pressure"

    
    cmd = 'sensortag 98:07:2d:40:bd:01 -n 1 -L'
    s = subprocess.check_output(cmd, shell=True)
    light8= s[s.find("Light:")+10:s.find(")")]
    print "OK sensor8 light sensor"
    print light8
    print "\n"

except Exception:
    print "Something wrong in Sensortag8"

try:
    dist = distance()
    print("Measured Distance = %.1f cm" % dist)
    time.sleep(1)

except Exception:
    print "Something wrong in Ultrasonic sensor"

time.sleep(1.0)
    
try:
    Temperature =urllib.urlopen("https://api.thingspeak.com/update?api_key=2LO1O35M00UFCTXE&field1="+str(etemp1)+"&field2="+str(etemp2)+"&field3="+str(etemp3)+"&field4="+str(etemp4)+"&field5="+str(etemp5)+"&field6="+str(etemp6)+"&field7="+str(etemp7)+"&field8="+str(etemp8));
    Humidity =urllib.urlopen("https://api.thingspeak.com/update?api_key=3JTLJB6IS6NPK90E&field1="+str(RHhumidity1)+"&field2="+str(RHhumidity2)+"&field3="+str(RHhumidity3)+"&field4="+str(RHhumidity4)+"&field5="+str(RHhumidity5)+"&field6="+str(RHhumidity6)+"&field7="+str(RHhumidity7)+"&field8="+str(RHhumidity8));
    Pressure =urllib.urlopen("https://api.thingspeak.com/update?api_key=P7YY48GW5LCH9SU6&field1="+str(baromilli1)+"&field2="+str(baromilli2)+"&field3="+str(baromilli3)+"&field4="+str(baromilli4)+"&field5="+str(baromilli5)+"&field6="+str(baromilli6)+"&field7="+str(baromilli7)+"&field8="+str(baromilli8));
    Sunlight =urllib.urlopen("https://api.thingspeak.com/update?api_key=1LCVAVX46RT507NL&field1="+str(light1)+"&field2="+str(light2)+"&field3="+str(light3)+"&field4="+str(light4)+"&field5="+str(light5)+"&field6="+str(light6)+"&field7="+str(light7)+"&field8="+str(light8));
    Distance =urllib.urlopen("https://api.thingspeak.com/update?api_key=THIWV0DLQ1SZCGH2&field1="+str(dist));
    Battery =urllib.urlopen("https://api.thingspeak.com/update?api_key=AI2WEU90SIMMVMNZ&field1="+str(bat1)+"&field2="+str(bat2)+"&field3="+str(bat3)+"&field4="+str(bat4)+"&field5="+str(bat5)+"&field6="+str(bat6)+"&field7="+str(bat7)+"&field8="+str(bat8));





except Exception:
    print "Something wrong in sending"





if Temperature!=0:
    call("sudo shutdown -h now", shell=True)
