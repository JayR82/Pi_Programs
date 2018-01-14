import os
from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
i = 1
sleeper = 30
destFolder = '/home/pi/Desktop/Bilder1/'

print "start"
print destFolder

if not os.path.exists(destFolder):
  os.makedirs(destFolder)

while True:
  try:
    camera.start_preview()
    sleep(1)
    camera.capture(destFolder + 'Bild%04d.jpg' %i)
    sleep(1)
    camera.stop_preview()
    sleep(sleeper)
    i=i+1
  except KeyboardInterrupt:
    sleep(1)
    print "ende"
                                
    
    
