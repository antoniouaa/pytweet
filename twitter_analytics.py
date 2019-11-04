import pandas as pd
import ast
from collections import Counter

tweets = pd.read_csv("saved_tweets.csv")
tweets.columns = ["hashtags", "text", "user", "location"]

list_hashtag_strings = [entry for entry in tweets.hashtags]
list_hashtag_lists = ast.literal_eval(",".join(list_hashtag_strings))
hashtag_list = [ht.lower() for list_ in list_hashtag_lists for ht in list_]

list_location_strings = [entry for entry in tweets.location]

counter_hashtags = Counter(hashtag_list)
print(counter_hashtags.most_common(20))
counter_locations = Counter(list_location_strings)
print(counter_locations.most_common(20))

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

