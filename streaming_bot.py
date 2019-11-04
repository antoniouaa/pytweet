from twython import TwythonStreamer
import csv

def process_tweet(tweet):
    d = {}
    try:
        d["hashtags"] = [hashtag["text"] for hashtag in tweet["entities"]["hashtags"]]
        d["text"] = tweet["text"]
        d["user"] = tweet["user"]["screen_name"]
        d["user_loc"] = tweet["user"]["location"]
        print(d)
        return d
    except:
        pass

class StreamingBot(TwythonStreamer):
    def on_success(self, data):
        tweet_data = process_tweet(data)
        self.save_to_csv(tweet_data)

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()

    def save_to_csv(self, tweet):
        with open("saved_tweets.csv", "a", encoding="utf-8") as infile:
            writer = csv.writer(infile)
            try:
                if tweet.values():
                    writer.writerow(list(tweet.values()))
            except:
                pass
