import search_tweet
import sys
from datetime import datetime, timedelta
from time import sleep

# MAIN PROGRAM
if len(sys.argv) == 1:
	n_tweet = 50
else:
	n_tweet = int(sys.argv[1])

DATABASE_DIR = ''
twitter_scrap = search_tweet.ScrapperBot(DATABASE_DIR)

tweet_date = str(datetime.now().strftime("%Y-%m-%d"))
hashtags = ['#coronavaccine', '#antivaxxer', '#vaccine', '#antivax', '#antivaccine', '#vaccinedeath']
query = f"({' OR '.join(hashtags)}) since:{tweet_date} lang:en -filter:retweets"

result = twitter_scrap.get_tweets(query, n_tweet=n_tweet)
# for key, value in result.items():
#     print(key, value, end="\n")
print(f"{len(result['tweet'])} tweets have been retrieved at {datetime.now()}")

twitter_scrap.store()
twitter_scrap.close_connection()

