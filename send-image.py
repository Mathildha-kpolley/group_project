import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart





#img_file = "/home/pi/Desktop/cookies/image.jpg"
img_file = "me.jpg"
recipient = "doorbellsmart5@gmail.com"

# Read the username and password and strip extra whitespace
# Make sure to .gitignore username.txt and password.txt!
username = open("username.txt", 'r').read().strip()
password = open("password.txt", 'r').read().strip()
print (username)
print (password)
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

print (username, password, recipient)
