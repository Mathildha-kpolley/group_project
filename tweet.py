import tweepy
from keys import *

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(akey, asecret)

api = tweepy.API(auth)

api.update_status('Doorbell Notification2')


api.update_with_media('image1.jpg', 'Someone else at your door')

print 'tweet successfully sent'
