
import  sqlite3

db = "twitterDB.db"

def create_db():
    #creating data model for twitter user account
    try:
        with sqlite3.connect(db) as conn:

            conn.execute('''CREATE TABLE IF NOT EXISTS USER
                     (ID INT PRIMARY KEY     NOT NULL,
                      NAME           CHAR(50)    NOT NULL,
                      SCREEN_NAME    CHAR(50)     NOT NULL,
                      DESCRIPTION    TEXT,
                      LOCATION       TEXT );''')

            conn.execute('''CREATE TABLE IF NOT EXISTS USER_TWEETS
                     (ID INT PRIMARY KEY     NOT NULL,
                       SOURCE        CHAR(100)    NOT NULL,
                       CREATED_AT    DATETIME     NOT NULL,
                       TEXT          TEXT,
                       FAVORITE_COUNT   INT,
                       RETWEET_COUNT INT,
                       USER_ID INT,
                       FOREIGN KEY(USER_ID) REFERENCES USER(ID));''')

            conn.execute('''CREATE TABLE IF NOT EXISTS USER_FOLLOWING
                        ( USER_ID INT,
                          FOLLOWING_ID INT,
                          FOREIGN KEY(USER_ID) REFERENCES USER(ID),
                          FOREIGN KEY(FOLLOWING_ID) REFERENCES USER(ID));''')

            conn.execute('''CREATE TABLE IF NOT EXISTS USER_FAVORITE_TWEETS
                        ( USER_ID INT,
                          TWEET_ID INT,
                          FOREIGN KEY(USER_ID) REFERENCES USER(ID),
                          FOREIGN KEY(TWEET_ID) REFERENCES USER(USER_TWEETS));''')
    except conn.Error as e:
        print("Error sql: creating schema %s" % e)

if __name__== "__main__":
    create_db()