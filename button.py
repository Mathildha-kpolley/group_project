from gpiozero import LED, Button
from signal import pause
import picamera
import os, time
import tweepy
from keys import *
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey, asecret)
api = tweepy.API(auth)

def cam():
    print("About to take a picture.")
    with picamera.PiCamera() as camera:
    #camera = picamera.PiCamera()
        camera.resolution = (1280,720)
        id = str(time.time())
        name = "image_" + id + ".jpg"
        print (name)
        camera.capture(name)
        print("picture taken")
        sendTweet(name)
        sendEmail(name)
    
def sendTweet(name):
    api.update_with_media(name, 'Someone else at your door')
    print ('tweet successfully sent')
    
def sendEmail(img_file):
    recipient = "doorbellsmart5@gmail.com"

    # Read the username and password and strip extra whitespace
    # Make sure to .gitignore username.txt and password.txt!
    username = open("username.txt", 'r').read().strip()
    password = open("password.txt", 'r').read().strip()
    img = open(img_file, 'rb').read()

    if username and password and img:
        msg = MIMEMultipart()
        msg['Subject'] = 'DoorBell Notification'
        msg['From'] = username
        msg['To'] = recipient

        text = MIMEText("Someone at your Door")
        msg.attach(text)
        image = MIMEImage(img, name=os.path.basename(img_file), _subtype="jpg")
        msg.attach(image)
        
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(username, password)
        s.sendmail(username, recipient, msg.as_string())
        s.quit()

    print ("sent email to "+recipient)

led = LED(17)
button = Button(2)

button.when_pressed = lambda:led.on
button.when_released =lambda: led.off
button.when_pressed = lambda:cam()

input()






