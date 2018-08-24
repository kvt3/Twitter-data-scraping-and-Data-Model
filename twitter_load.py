try:
    import json
except ImportError:
    import simplejson as json
import tweepy
import sys
import sqlservice as db


'''
trying to get the twitter api object
'''
try:
    # Variables that contains the user credentials to access Twitter API
    ACCESS_TOKEN = '157287702-Rz14dJZsfssMhTlKxjHTMuoYHL5n5iWaV7l0c0I6'
    ACCESS_SECRET = 'yRur3oDWvnz2muHkbDK44URlLvArj4ctYF6NR0QsXbcxS'
    CONSUMER_KEY = 'ojCOcP37UjcVDu7sYBChw9TB8'
    CONSUMER_SECRET = 'Go11IM8dlViGIJCq0XGL56QQIbsgTARmRycMkcqhs6ZREllm2m'

    auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)
    api = tweepy.API(auth,wait_on_rate_limit=True)
except tweepy.TweepError as e:
    print("Error when retriving twitter api: %s" % e)


''''
#Retrive the basic information of user from twitter
#Inserts it into USER table
'''
def store_user_info(user):
    db.insert_user_info(user)


'''
Retrive the tweets information of user from twitter.
Inserts it into USER_TWEETS table.
'''
def stote_user_tweets(user):
    try:
        for tweet in tweepy.Cursor(api.user_timeline,
                                   screen_name=user.screen_name,
                                   result_type="recent",
                                   tweet_mode ='extended',
                                   include_entities=True,lang="en").items():
            db.insert_tweets(tweet, user)
    except tweepy.TweepError as e:
        print("Error when retriving tweet: %s" % e)


''''
#retrive the information of users whom the user is following from twitter
#Inserts it into USER table and USER_FOLLOWING table
'''
def store_user_following(user):
    try :
        for follows in tweepy.Cursor(api.friends,
                                     screen_name=user.screen_name,
                                     result_type="recent",
                                     tweet_mode='extended',
                                     include_entities=True,lang="en").items():
            db.insert_followers(user, follows)
    except tweepy.TweepError as e:
        print("Error when retriving followers: %s" % e)


''''
#retrive the information of user likes tweets from twitter
#Inserts it into USER_TWEETS and USER_FAVORITE_TWEETS table
'''
def store_liked_tweets(user):
    try:
        for favorite in tweepy.Cursor(api.favorites,screen_name=user.screen_name,
                                     result_type="recent",tweet_mode='extended',
                                     include_entities=True,lang="en").items():
            db.insert_favorite_tweets(user,favorite)
    except tweepy.TweepError as e:
        print("Error when retriving favorite tweets: %s" % e)


if __name__== "__main__":
    try:
        tweet_handle = sys.argv[1]
        user = api.get_user(screen_name=tweet_handle)
    except tweepy.TweepError as e:
        print('get_user: failed to get user %s: %s', tweet_handle, e.message)

    store_user_info(user)
    stote_user_tweets(user)
    store_user_following(user)
    store_liked_tweets(user)
