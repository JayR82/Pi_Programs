from picamera import PiCamera
from os import system
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/testbild.jpg')
sleep(2)
camera.stop_preview()

		
    
    
    
