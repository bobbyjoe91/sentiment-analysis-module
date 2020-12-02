import search_tweet
import sys
from datetime import datetime, timedelta
from time import sleep

# MAIN PROGRAM
if len(sys.argv) == 1:
	n_tweet = 50
else:
	n_tweet = int(sys.argv[1])


twitter_scrap = search_tweet.ScrapperBot('./tweetDatabase.db')

tweet_date = str(datetime.now().strftime("%Y-%m-%d"))
hashtags = ['#coronavaccine', '#antivaxxer', '#vaccine', '#antivax', '#antivaccine', '#vaccinedeath']
query = f"({' OR '.join(hashtags)}) since:{tweet_date} lang:en -filter:retweets"

result = twitter_scrap.get_tweets(query, n_tweet=n_tweet)
# for key, value in result.items():
#     print(key, value, end="\n")
print(f"{len(result['tweet'])} tweets have been retrieved at {datetime.now()}")

twitter_scrap.store()
twitter_scrap.close_connection()

# start_time = datetime.now()
# while datetime.now()-start_time <= timedelta(seconds=3600*6, microseconds=0):
# 	get_time = datetime.now()
# 	twitter_scrap = search_tweet.ScrapperBot('./bobby.cool00763_final.db')

# 	tweet_date = str(get_time.strftime("%Y-%m-%d"))
# 	hashtags = ['#coronavaccine', '#antivaxxer', '#vaccine', '#antivax', '#antivaccine', '#vaccinedeath']
# 	query = f"({' OR '.join(hashtags)}) since:{tweet_date} lang:en -filter:retweets"

# 	result = twitter_scrap.get_tweets(query, n_tweet=n_tweet)
# 	twitter_scrap.store()
# 	twitter_scrap.close_connection()

# 	print(f"{len(result['tweet'])} tweets have been retrieved at {get_time}")
# 	sleep(900)

