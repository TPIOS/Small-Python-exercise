from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

# consumer_key = 'PHG9tkvUpVdCLHuluiQFAA'
# consumer_secret = 'dqpNZnLTwteX1YGnQ0VQ3Pv2up6ensEFeaS8MnQDE'
# access_token = '38744894-0TBISZIcuDE5Sm1VI6VqZXGVYH9Yjn63e9ZM8v7ei'
# access_token_secret = 'g6EIhezIPuIcrPzM1jDyqqjXMH25EDeJncHaxvQeu0'

consumer_key = '3at3pt2BImiNK93JSQgeIU1u6'
consumer_secret = 'k3xXVW5g8ZT7YgZ1sJwSEBqWh8GFGr1adD4q2H77ushGVXnkEs'
access_token = '1017453150897180672-3OkVq4reDseKzpqyOh8R8PlBhtjZDb'
access_token_secret = 'H9CLdiqaOwFniAfMCN2mDUs7iA26h417viDSNSYJdaq4w'

class StdOutListener(StreamListener):
    def on_data(self, data):
        with open("twitter.json", 'a') as tf:
            tf.write(data)
        return
    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['Apple watch'])
