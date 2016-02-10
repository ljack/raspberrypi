#!/usr/bin/python
# src https://learn.sparkfun.com/tutorials/raspberry-pi-twitter-monitor/dissecting-the-code

from sense_hat import SenseHat
import time
from twython import TwythonStreamer

sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
tweet_color = (255,255,255)
msg = "Starting 8x8 tweeter!!"
print msg
sense.show_message(msg , text_colour=tweet_color)


# Search terms
# for doc see https://dev.twitter.com/streaming/reference/post/statuses/filter
TERMS = '#yes,jarkkolietolaht,Raspberry_Pi,Cloud9IDE'

# Twitter application authentication
APP_KEY = 'X'
APP_SECRET = 'X'
OAUTH_TOKEN = 'X-X'
OAUTH_TOKEN_SECRET = 'X'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
                        msg = data['text'].encode('utf-8')
                        print msg
                        print
                        sense.show_message(msg, text_colour=tweet_color)
                        time.sleep(0.5)


# Create streamer
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        print "Done"
        
        
