import tweepy, time, random

CONSUMER_KEY = 'xxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('lines.txt','r')
f=filename.readlines()
filename.close()

for line in f:
     api.update_status(line)
     print line
     time.sleep(3700)