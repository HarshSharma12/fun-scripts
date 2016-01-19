"""
Created on Mon Dec 14 15:12:32 2015
@author: HarshSharma12

Searches twitter for the keyword 'help' and 
replies to the user with the message 'May the 
force be with you.' Runs once every hour

Follow on twitter @forcehelps
"""

#!/usr/local/bin/python2.7
import oauth2
import time
import urllib2
import json
from twitter import *
while(1):
    url1 = "https://api.twitter.com/1.1/search/tweets.json"
    params_stat = {
    "oauth_version": "1.0",
    "oauth_nonce": oauth2.generate_nonce(),
    "oauth_timestamp": str(int(time.time()))
    }
    
    con_key="Enter your Consumer Key here"
    con_secret="Enter your Consumer Secret here"
    token_key = "Enter your Access Token here"
    token_secret="Enter your Access Token Secret here"
    t = Twitter(auth=OAuth(token_key, token_secret, con_key, con_secret))
    
            
    consumer = oauth2.Consumer(key=con_key, secret=con_secret)
    token = oauth2.Token(key=token_key, secret=token_secret)
    params_stat["oauth_consumer_key"] = consumer.key
    params_stat["oauth_token"] = token.key
    
    params = params_stat
    
    for i in range(1):
        url = url1
        req = oauth2.Request(method="GET", url=url, parameters=params)
        signature_method = oauth2.SignatureMethod_HMAC_SHA1()
        req.sign_request(signature_method, consumer, token)
        headers = req.to_header()
        url = req.to_url()
        #print headers
        #print url
    
    
    searchStr = 'help'
    noOfTweets = 5;
    tweetLang = 'en'
    
    for i in range(1):
        url = url1
        params["q"] = searchStr
        params["count"] = noOfTweets
        params["lang"] = tweetLang
        req = oauth2.Request(method="GET", url=url, parameters=params)
        signature_method = oauth2.SignatureMethod_HMAC_SHA1()
        req.sign_request(signature_method, consumer, token)
        headers = req.to_header()
        url = req.to_url()
        response = urllib2.Request(url)
        proxy = urllib2.ProxyHandler({'https': 'proxy-url, if any'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        data = json.load(urllib2.urlopen(response))
    tweets = []
    userIds=[]
    for a in range(noOfTweets):
        if(data['statuses'][a]['text'][0]!='@' or (data['statuses'][a]['text'][0].upper()!='R' and data['statuses'][a]['text'][1].upper()!='T')):
           tweets.append('.@'+ str(data['statuses'][a]['user']['screen_name']) + ' May the force be with you.')
           userIds.append(str(data['statuses'][a]['id']))
    
    print tweets
    print userIds
    
    for a in range(noOfTweets):
        print tweets[a]
        print userIds[a]
        t.statuses.update(status=tweets[a], in_reply_to_status_id=userIds[a])
        time.sleep(10)
    
    #Repeat after 60 min
    time.sleep(60*60)
