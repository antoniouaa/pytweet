import pandas as pd
import ast
import sys
from collections import Counter

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

