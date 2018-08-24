from flask import Flask,jsonify
import sqlservice as db

app = Flask(__name__)

#the service will provide all the tweets tweeted by user
@app.route('/api/getTweets/<string:user_name>', methods=['GET'])
def get_tweets(user_name):
    result = db.get_tweets(user_name)
    return jsonify(result)

#the service will provide all the tweets liked by user
@app.route('/api/getFavoriteTweets/<string:user_name>', methods=['GET'])
def get_favorite_tweets(user_name):
    result = db.get_favorite_tweets(user_name)
    return jsonify(result)

#the service will provide all the list of users followed by user
@app.route('/api/getFollowings/<string:user_name>', methods=['GET'])
def get_followings(user_name):
    result = db.get_followings(user_name)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,port='8080')
