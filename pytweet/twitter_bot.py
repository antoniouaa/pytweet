from twython import Twython
from streaming_bot import StreamingBot
import pandas as pd
import json

def batch_query(query):
    post_ = {"user": [], "date": [], "text": [], "favorite_count": []}
    for status in python_tweets.search(**sample_query)["statuses"]:
        post_["user"].append(status["user"]["screen_name"])
        post_["date"].append(status["created_at"])
        post_["text"].append(status["text"])
        post_["favorite_count"].append(status["favorite_count"])

    df = pd.DataFrame(post_)
    df.sort_values(by="favorite_count", inplace=True, ascending=False)
    #df.to_csv("saved_tweets.csv", sep=",")
    return df

credentials = {
        "CONSUMER_KEY" : "ELtHFSlF6oyC62WoHvmi9pBTK",
        "CONSUMER_SECRET" : "gcfn0y6PVXBLAHbqCZhQFUBsteCWgPiF2BQnkbGPvUNoTQE3oF",
        "ACCESS_TOKEN" : "780845339796393984-FT9bNGCOwBlMYSuHy120zBF2g7yYcY0",
        "ACCESS_SECRET" : "LxX9ARDyFkWlwoGTZXAVjSdB90zB7J0mwT19guJSnUO6l"}

sample_query = {"q": "trump",
                "result_type": "popular",
                "count": 1000,
                "lang": "en"}


#python_tweets = Twython(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"])
#df = batch_query(sample_query)
#print(df.head(10))
#res = python_tweets.cursor(python_tweets.search, q="trump")

search_term = input("Search for: ")
stream = StreamingBot(credentials["CONSUMER_KEY"], credentials["CONSUMER_SECRET"], credentials["ACCESS_TOKEN"], credentials["ACCESS_SECRET"])
stream.statuses.filter(track=search_term)

