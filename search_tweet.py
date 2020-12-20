import config
import sqlite3
import tweepy

from wordprocessor import clean_tweet, vader_analyzer
from datetime import date, datetime

def insert_into(connection, cursor, table_name, colname, values):
    try:
        insert_query = f'''
            INSERT OR IGNORE INTO {table_name} ({', '.join(colname)}) 
            VALUES ({', '.join(['?']*len(colname))})
        '''
        cursor.executemany(insert_query, values)
        connection.commit()
    except:
        pass

class ScrapperBot:
    def __credit__(self):
        import json
        try:
            with open('./biodata.json') as biodata_json:
                bio = json.load(biodata_json)

            print(f"Developed by {bio['nama']}\n{bio['email']}")
        except:
            print('Biodata.json is not found. Whose program is this?')

    def __init__(self, db_path):
        # Connect to Twitter API
        self.auth = tweepy.OAuthHandler(config.api_public, config.api_private)
        self.auth.set_access_token(config.access_public, config.access_private)
        self.api = tweepy.API(self.auth)

        # Connect to database
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        # Update yesterday's Lastscraping status
        # if last scraping date isn't equal to today's date
        get_last_scraping_date = '''SELECT MAX(l.last_get) FROM Lastscraping l'''
        self.cursor.execute(get_last_scraping_date)
        last_scraping_date = self.cursor.fetchone()[0]

        if last_scraping_date != None: # suppose the Lastscraping table isn't empty
            last_scraping_date = last_scraping_date.split(' ')[0]

            today_date = str(date.today())

            if today_date != last_scraping_date:
                yesterday_status_update = f'''
                    UPDATE Lastscraping SET status = 0 
                    WHERE last_get <= strftime('{last_scraping_date} 23:59:59') 
                    AND status = 1
                '''
                self.cursor.execute(yesterday_status_update)
                self.connection.commit()

    def get_tweets(self, query, n_tweet=200):
        self.last_scraping = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S.000"))
        tweets = tweepy.Cursor(self.api.search, q=query, tweet_mode='extended').items(n_tweet)
        tweet_list = list(tweets)

        # Insert last_get and status of Lastscraping
        insert_into(
            self.connection, 
            self.cursor, 
            'Lastscraping',
            ['last_get', 'status'], 
            [(self.last_scraping, 1,),]
        )

        get_scraping_id = 'SELECT MAX(l.scraping_id) FROM Lastscraping l'
        self.cursor.execute(get_scraping_id)
        self.scraping_id = self.cursor.fetchone()

        self.result = {
            'tweet': [],
            'user': [],
            'sentiment': []
        }
        for tweet in tweet_list:
            user = tweet.user
            clean_tweet_text = clean_tweet(tweet.full_text)
            tweet_data = (
                tweet.id,
                user.id,
                tweet.created_at.strftime("%Y-%m-%d %H:%M:%S.000"),
                tweet.full_text,
                clean_tweet_text,
                self.scraping_id[0]
            )

            user_data = (
                user.id,
                user.name,
                user.screen_name,
                user.location,
                user.created_at.strftime("%Y-%m-%d %H:%M:%S.000"),
                user.followers_count,
                user.friends_count,
                int(user.verified)
            )

            sentiment_analysis = vader_analyzer(clean_tweet_text)
            polarity = sentiment_analysis[0]
            sentiment = sentiment_analysis[1]
            sentiment_data = (
                tweet.id,
                polarity['pos'],
                polarity['neg'],
                polarity['neu'],
                polarity['compound'],
                sentiment
            )

            self.result['tweet'].append(tweet_data)
            self.result['user'].append(user_data)
            self.result['sentiment'].append(sentiment_data)

        return self.result

    def store(self):
        # insert user_data to User
        insert_into(
            self.connection, 
            self.cursor, 
            'TwitterUser',
            ['userid', 'name', 'screenname', 'location', 'acccreated', 'follower', 'friend', 'verified'], 
            self.result['user']
        )

        # insert tweet data to Tweet
        insert_into(
            self.connection, 
            self.cursor,
            'Tweet', 
            ['tweetid', 'userid', 'createddate', 'tweet', 'cleantweet', 'scraping_id'], 
            self.result['tweet']
        )

        # insert sentiment scoring to Sentiment
        insert_into(
            self.connection,
            self.cursor,
            'Sentiment',
            ['tweetid', 'positive', 'negative', 'neutral', 'compound', 'sentiment'],
            self.result['sentiment']
        )

    def close_connection(self):
        self.cursor.close()
        self.connection.close()