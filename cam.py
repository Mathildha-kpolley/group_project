import picamera 


print("About to take a picture.")
#with picamera.PiCamera() as camera:
camera = picamera.PiCamera()
camera.resolution = (1280,720)
camera.capture("/home/pi/Desktop/cookies/newimage.jpg")
print("picture taken")

