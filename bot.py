import tweepy, random, time

CONSUMER_KEY = 'xxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxx' # Make sure access level is Read And Write in the Settings tab
ACCESS_KEY = 'xxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open('lines.txt','r') as filename:
    file_lines = filename.readlines()
random.shuffle(file_lines)
for line in file_lines:
     api.update_status(line)
     print line,
     time.sleep(300) #time is in seconds
