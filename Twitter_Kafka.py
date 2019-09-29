import json
import sys
import tweepy
from kafka import KafkaProducer, KafkaClient
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener
from configparser import ConfigParser
from utils import team_dict

class Twitter_stream(StreamListener):
    def __init__(self, api):
        self.api = api
        super(StreamListener, self).__init__()
        client = KafkaClient("localhost:9092")
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('utf-8'))

    def inData(self, data):
        text = json.loads(data)['text'].encode('utf-8')
        print(text)
        try:
            self.producer.send('twitterstream', data)
        except Exception as e:
            print(e)
            return False
        return True

    def inError(self, status_code):
        print("Error recieved in Kafka producer")
        return True
    
    def inTimeout(self):
        return True
    
    if __name__ == '__main__':

        PROJECT_HOME = 'D://GitHub/Twitter_Monitor'

    #authenticate

        config = ConfigParser()

        config.read(PROJECT_HOME + '.config/.credentials')

        consumer_key = config.get('auth', 'consumer_key')

        consumer_secret = config.get('auth', 'consumer_secret')

        access_token = config.get('auth', 'access_token')

        access_token_secret = config.get('auth', 'access_token_secret')



        auth = OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = API(auth)

    

        stream = Stream(auth, listener=TstreamListener(api))

 

        tracked = []

        for team in team_dict.keys():

            tracked.extend(team_dict[team]) 

        stream.filter(track=tracked, languages=['en'])