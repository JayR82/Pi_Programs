import os
from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
i = 4
timer1 = "10:16"
timer2 = "14:17"
timer3 = "17:58"

destFolder = '/home/pi/Desktop/Bilder/'
print "start"
print destFolder

if not os.path.exists(destFolder):
  os.makedirs(destFolder)

sleep(1)
camera.capture(destFolder + 'Testbild.jpg')

while True:
  now = datetime.now().strftime("%H:%M")
  if (now == timer1) or (now == timer2) or( now == timer3):
    try:
      print "do it"
      camera.start_preview()
      sleep(1)
      camera.capture(destFolder + 'Bild%04d.jpg' %i)
      sleep(1)
      camera.stop_preview()
      i=i+1
      sleep(22)
      sleep(20)
      sleep(20)
    except KeyboardInterrupt:
      sleep(1)
      print "ende"
  else:
    sleep(22)
    sleep(20)
    sleep(20)
                                
    
    
