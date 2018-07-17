from gpiozero import LED, Button
from signal import pause
import picamera
import os, time

from time import sleep




 
def cam():

     
    print("About to take a picture.")
    with picamera.PiCamera() as camera:
    #camera = picamera.PiCamera()
        camera.resolution = (1280,720)
	id = str(time.time())
        name = "/home/pi/Desktop/cookies/image_" + id +   ".jpg"
	camera.capture(name)
    print("picture taken")
   
	


led = LED(17)
button = Button(2)

button.when_pressed = lambda:led.on
button.when_released = led.off


button.when_pressed = lambda:cam()
input ()



