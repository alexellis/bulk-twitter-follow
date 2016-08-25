import tweepy
from config import config

import fileinput

lines = []
for line in fileinput.input():
    if(len(line) > 0):
        lines.append(line)

if(config == None):
    print "Mount a config.py file into the container"
    quit()

print "Read captains list: " + str(len(lines))

auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_token"], config["access_token_secret"])

api = tweepy.API(auth)

me = api.me()
users = lines

# Backwards-compatibility with v0.1 of program.
if "appear_in_my_feed" not in config:
    config["appear_in_my_feed"] = True

for user in users:
    status = api.show_friendship(target_screen_name = user)
    if(status[0].screen_name != status[1].screen_name):
        if(status[1].following == False):
            print(status[1].screen_name + " is not following you.")

        if(status[0].following == False):
            try:
                api.create_friendship(screen_name = status[1].screen_name, follow = config["appear_in_my_feed"])
                print("Following: " + status[1].screen_name)
            except tweepy.TweepError as e:
                print(e)
