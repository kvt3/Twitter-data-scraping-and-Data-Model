import sqlite3

db = "twitterDB.db"

def insert_tweets(tweet, user):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('''INSERT OR IGNORE INTO USER_TWEETS VALUES (?,?,?,?,?,?,?)''',
                (tweet.id, tweet.source, str(tweet.created_at),
                tweet.full_text, tweet.favorite_count,
                tweet.retweet_count, user.id))
    except conn.Error as e:
        print("sql error: inertig tweets%s", e)


def insert_user_info(user):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('''INSERT OR IGNORE INTO USER VALUES (?,?,?,?,?)''', (
                user.id, user.name, user.screen_name,
                user.description, user.location))
    except conn.Error as e:
        print("sql error inserting user info: %s", e)

def insert_followers(user,follows):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('''INSERT OR IGNORE INTO USER VALUES (?,?,?,?,?)''', (
                follows.id, follows.name, follows.screen_name,
                follows.description, follows.location))

            conn.execute('''INSERT INTO USER_FOLLOWING VALUES (?,?)''', (user.id, follows.id))
    except conn.Error as e:
        print("sql error inserting followings: %s", e)


def insert_favorite_tweets(user,favorite):
    try:
        with sqlite3.connect(db) as conn:
            conn.execute('''INSERT OR IGNORE INTO USER_TWEETS VALUES (?,?,?,?,?,?,?)''', (
                favorite.id, favorite.source, str(favorite.created_at),
                favorite.full_text, favorite.favorite_count,
                favorite.retweet_count, favorite.user.id))

            conn.execute('''INSERT INTO USER_FAVORITE_TWEETS VALUES (?,?)''', (user.id, favorite.id))
    except conn.Error as e:
        print("sql error inserting favorite tweets: %s", e)

def get_tweets(user_name):
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute('''select ID,SOURCE,CREATED_AT,TEXT,FAVORITE_COUNT,RETWEET_COUNT,USER_ID
                              from USER_TWEETS
                               where USER_ID = (select USER_ID from USER where SCREEN_NAME = ?)''', [user_name])
            result = {'tweets': [dict(zip([column[0] for column in cursor.description], row))
                                 for row in cursor.fetchall()]}
    except conn.Error as e:
        print("sql error: %s", e)
    return result

def get_favorite_tweets(user_name):
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute('''select * from USER_TWEETS
                                    where ID in( select TWEET_ID from USER_FAVORITE_TWEETS
                                    where USER_ID = (select ID from USER where SCREEN_NAME = ?))''', [user_name])
            result = {'tweets': [dict(zip([column[0] for column in cursor.description], row))
                                 for row in cursor.fetchall()]}
    except conn.Error as e:
        print("sql error: %s", e)
    return result

def get_followings(user_name):
    try:
        with sqlite3.connect(db) as conn:
            cursor = conn.cursor()
            cursor.execute('''select * from User
                                      where ID in (select following_id from USER_FOLLOWING
                                      where USER_ID = (select ID from USER where SCREEN_NAME = ?))''', [user_name])
            result = {'tweets': [dict(zip([column[0] for column in cursor.description], row))
                                 for row in cursor.fetchall()]}
    except conn.Error as e:
        print("sql error: %s", e)
    return result

