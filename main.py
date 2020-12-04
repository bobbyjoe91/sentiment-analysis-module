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

tweet_date = str(datetime.now().strftime("%Y-%m-%d")) # set date here
keywords = [''] # put the search keywords (hashtags, ordinary keywords, etc.) here

filters = f"since:{tweet_date} lang:en -filter:retweets" # twitter search filter
query = f"({' OR '.join(keywords)}) {filters}"

result = twitter_scrap.get_tweets(query, n_tweet=n_tweet)

# uncomment the code below to print all tweet retrieved
# for key, value in result.items():
#     print(key, value, end="\n")

print(f"{len(result['tweet'])} tweets have been retrieved at {datetime.now()}")

twitter_scrap.store()
twitter_scrap.close_connection()

