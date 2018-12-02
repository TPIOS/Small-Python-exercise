import json
import sys
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk import FreqDist

tweets = json.loads(open('twitter.json').read())

tweet_text = [tweet['text'] for tweet in tweets]
tweet_source = [tweet['source'] for tweet in tweets]
tweet_geo = [tweet['geo'] for tweet in tweets]
tweet_locations = [tweet['place'] for tweet in tweets]
hashtags = [ hashtag['text'] for tweet in tweets for hashtag in tweet['entities']['hashtags'] ]

print(tweet_text)
print(tweet_locations)
print(tweet_geo)
print(hashtags)

tweet_tokens = []
for tweet in tweet_text:
    tweet_tokens.append(word_tokenize(tweet))

Topic_distribution = FreqDist(tweet_tokens)
Topic_distribution.plot(50, cumulative=False)


Topics = []
for tweet in tweet_text:
    tagged = nltk.pos_tag(word_tokenize(tweet))
    Topics_token = [word for word, pos in tagged if pos in ['NN', 'NNP']]
    print(Topics_token)

klout_scores = [(tweet['user']['followers_count']/ tweet['user']['friends_count'],tweet['user']) for tweet in tweets ]
print(klout_scores)
