from Load_TC_Sentiment_mod import sentiment
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

import Load_TC_Sentiment_mod as s

# consumer key, consumer secret, access token, access secret.
ckey = ""
csecret = ""
atoken = ""
asecret = ""


class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)

            tweet = all_data["text"]
            sentiment_value, confidance = s.sentiment(tweet)
            print(tweet, sentiment_value, confidance)
            if confidance*100 > 80:
                output = open("twitter-out.txt", 'a')
                output.write(sentiment_value)
                output.write('\n')
                output.close()

            return True
        except:
            return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
