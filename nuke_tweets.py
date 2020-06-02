#!/bin/python3
"""
A python script to nuke tweets in your account

@requirements: tweepy, python-dotenv
@author: github.com/actualdragon
"""
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv

import tweepy
import csv

# Load env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Access env variables
consumer_key = getenv('CONSUMER_KEY')
consumer_secret = getenv('CONSUMER_SECRET')
access_token = getenv('ACCESS_TOKEN')
access_token_secret = getenv('ACCESS_TOKEN_SECRET')
#tweets_to_keep1 = getenv('TWEETS_TO_KEEP').split(',')
tweets_csv = getenv('PATH_TO_TWEETS')
 
###
tweet_t_k = getenv('TWEETS_TO_KEEP')
tweets_to_keep = []
with open(tweet_t_k, newline = '', encoding='utf8') as csvfile:
  reader = csv.reader(csvfile)
  next(reader, None)
  tweets_to_keep1 = list(reader)
#print(tweets_to_keep)
for row in tweets_to_keep1:
  if 'RT' not in row[1]:
    tweets_to_keep.append(row[0])
#print(tweets_to_keep)

#   for row in reader:
#     #print(row)
#     tweets_to_keep.append(row)
# print(tweets_to_keep) 
#####   

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print('OAuth request sent')
api = tweepy.API(auth)

print('OAuth successful, now loading tweets archive')
with open(tweets_csv, newline = '', encoding='utf8') as f:
  reader = csv.reader(f)

  # Skip header
  next(reader, None)

  # Convert CSV to list
  tweets_list = list(reader)

print('Nuking...')
for tweet in tweets_list:

  # tweet[0] is the tweet_id column
  tweet_id = tweet[1] 

  if (tweet_id in tweets_to_keep):
    # Do not delete tweet
    print('[ 0 ] tweet with id %s' %(tweet_id))
  else:

    try:

      # Delete the tweet
      api.destroy_status(tweet_id)
      print('[ - ] tweet with id %s' %(tweet_id))
      if tweepy.TweepError:
        pass
      else:
        pass
    except tweepy.TweepError as e:
      print(e.reason)

print('Mission complete!')
