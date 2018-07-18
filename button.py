from gpiozero import LED, Button
from signal import pause
import picamera
import os, time
import tweepy
from keys import *
from time import sleep


auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey, asecret)

api = tweepy.API(auth)

global name
name = "image1.60.jpg"
def cam():

    print("About to take a picture.")
    with picamera.PiCamera() as camera:
    #camera = picamera.PiCamera()
        camera.resolution = (1280,720)
	id = str(time.time())
	global name
        name = "image_" + id + ".jpg"
	print (name)
	camera.capture(name)
    print("picture taken")
    global name
    print (name)
    api.update_with_media(name, 'Someone else at your door')

    print ('tweet successfully sent')


led = LED(17)
button = Button(2)

button.when_pressed = lambda:led.on
button.when_released =lambda: led.off

button.when_pressed = lambda:cam()



#api.update_status('Doorbell Notification2')
input()

