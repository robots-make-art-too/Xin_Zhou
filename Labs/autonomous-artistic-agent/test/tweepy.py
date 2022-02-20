import tweepy
import time
import os
# import imutils
#import ssl
#import json 


tokens = [] #tweepy key list
with open ('file.text','r') as f: #read file
    for line in f:  
        tokens.append(line.strip()) # add word on the end of list
#set key
consumer_key = tokens[0] 
consumer_secret = tokens[1]
access_token = tokens[2]
access_token_secret = tokens[3]
#login twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#### post image