import pandas as pd
import ast
import sys
from collections import Counter

def create_heatmap():
    from geopy.geocoders import Nominatim
    import gmplot

    geolocator = Nominatim(user_agent="twitter_bot")

    coordinates = {"latitude": [], "longitude": []}
    for count, user_loc in enumerate(tweets.location):
        try:
            location = geolocator.geocode(user_loc)
            if location:
                coordinates["latitude"].append(location.latitude)
                coordinates["longitude"].append(location.longitude)
        except:
            pass

    gmap = gmplot.GoogleMapPlotter(30, 0, 3)
    gmap.heatmap(coordinates["latitude"], coordinates["longitude"], radius=20)
    gmap.draw("trump_heatmap.html")

try:
    tweets = pd.read_csv("saved_tweets.csv")
except FileNotFoundError as fnfe:
    print("saved_tweets.csv doesn't exist")
    sys.exit()
tweets.columns = ["hashtags", "text", "user", "location"]

list_hashtag_strings = [entry for entry in tweets.hashtags]
list_hashtag_lists = ast.literal_eval(",".join(list_hashtag_strings))
hashtag_list = [ht.lower() for list_ in list_hashtag_lists for ht in list_]

from math import isnan
list_user_loc = []
for entry in tweets.location:
    try:
        if isnan(entry):
            pass
    except:
        list_user_loc.append(entry)

list_users = [entry for entry in tweets.user]

list_text = [entry for entry in tweets.text]
average_text_length = int(sum([len(t) for t in list_text]) / len(list_text))

counter_hashtags = Counter(hashtag_list)
counter_users = Counter(list_users)
counter_user_loc = Counter(list_user_loc)

print(f"Most Popular Hashtags: {counter_hashtags.most_common(20)}")
print(f"Number of users: {sum(counter_users.values())}")
print(f"Number of tweets: {len(list_text)}")
print(f"Average length of tweet: {average_text_length}")
print(f"Most Popular User Loc: {counter_user_loc.most_common(1)}")

#create_heatmap()
