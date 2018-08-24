# Twitter-data-scraping-and-Data-Model
The application will load the data into database. Through rest services you can get the information of user in JSON format.

Info: The application will load the data into database. Through rest services you can get the information of user in JSON format.
      The data retrving for perticular account are user information location, description, name, user tweets, user following 
      and user liked tweets.

Note: Mysql data is greate choice to store the information. I am using sqlite database for demo purpose. 
      Make sure you have following python package install otherwise install using pip command
      -python 3.5+
      -sqlite3
      -tweepy
      -flask(Flask,jsonify)
      -json

DataModel:
Tables:
USER
USER_TWEETS
USER_FOLLOWING
USER_FAVORITE_TWEETS

Relationships:
one to many:
	USER to USER_TWEETS
	USER to USER_FOLLOWINGS
	USER to USER_FAVORITE_TWEETS

Find the image in pdf.

modules:
init_service.py: Create sqlite database with schema
twitter_load.py: Connect with tweeter developer api to retrive the data.
sqlservice.py:  All database related query. inserting into db and selecting from db
dataservice.py: This is the rest service interface. This will take the http request and return result as JSON object   


commands to run program:
//------Create database schema-------//
>python3.6 init_service.py

//---- Load the data from twitter account to database for given user "twitter_handel e.g kalyanitaru"
// this will take 2 to 5 min, you can add as many user as you want
>python3.6 twitter_load.py <twitter_handel> 

//---start service on 8080 port------//
>python3.6 dataservice.py&

//--- get JSON object using http request ---//
> curl -i http://localhost:8080/api/getTweets/<twitter_handel>
> curl -i http://localhost:8080/api/getFollowings/<twitter_handel>
> curl -i http://localhost:8080/api/getFavoriteTweets/<twitter_handel>
