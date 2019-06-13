from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
# access_token="3nVuSoBZnx6U4vzUxf5w"

Consumer_key="3nVuSoBZnx6U4vzUxf5w"
Consumer_secret="Bcs59EFbbsdF6Sl9Ng71smgStWEGwXXKSjYvPVt7qys"
access_token="eyJz93a...k4laUWw"
access_token_secret="GEbRxBN...edjnXbL"

auth=OAuthHandler(Consumer_key,Consumer_secret)
# auth.set_access_token(access_token,access_token_secret)
# stream=Stream(auth,1)
# stream.filter(track=['python','javascript','ruby'])

tweets_data_path="C:/Users/Yogesh Kumar Ahuja/Desktop/twitter_data.txt"
tweets_data=[]
tweets_file=open(tweets_data_path,"r")
for line in tweets_file:
    try:
        tweet=json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))

tweets=pd.DataFrame()
tweets['text']=map(lambda tweet:tweet['text'],tweets_data)
tweets['lang']=map(lambda tweet:tweet['lang'],tweets_data)
tweets['Country']=map(lambda tweet:tweet['place']['Country'] if tweet['place']!=None else ,tweets_data)

