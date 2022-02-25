import time
import os
import sys
import tweepy
import BuildSupper

tokens = [] #tweepy key list
with open ('file.txt','r') as f: #read file
    for line in f:  
        tokens.append(line.strip()) # add word on the end of list
#set key
bearer_Token = tokens[0]
consumer_key = tokens[1] 
consumer_secret = tokens[2]
access_token = tokens[3]
access_token_secret = tokens[4]
#login twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#### post image
BuildSupper.buildImage()
api.update_status_with_media('Hi, what is you supper today?','today.jpg')
