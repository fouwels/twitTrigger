from time import sleep
import tweepy
import json 

consumer_key="NiUgmXPjRmB5FEYKFN4iFv4Ya"
consumer_secret="2wLJutH12hrn6h9h2IOIPzaFSlgx2hh56L0up8h52Y3kOTgn1y"

access_token="475287853-uoacekXZDEGqe7U3kWbEf8DgoBH6cFS8rryF75wF"
access_token_secret="3G74WyAzW6EdoDQfsxoqZvuCNA6dLx2Eq03rZRJlVOKr2"

consumer_key2="AiyQbVyTd0XxAm5lZGCJL2taN"
consumer_secret2="y6mKZOEKb7rgcUuSa0pVGhDq4ixJDNPwQ72jEo8pKAd4vthQiD"

access_token2="475287853-SfNQ796MkKlrMXqCqbF3IomjRly1SEP7QWE0RmHC"
access_token_secret2="BsiOVoOyyCACg77RsoGcTgeMEo7OsQYi7th5n446gToCp"

#api = tweepy.API(auth)

#lastid = 0;

#fobj = open('dump.txt', 'w')
#while True:
#	print api.me().name
#	ment = api.mentions_timeline(count=1)
#	lastid = ment[0].id
	
#	if ment[0].id != lastid:
#		fobj.write(ment[0].text)
#		print ment[0].text
#		lastid = ment[0].id
#	else:
#		print "no new since id: ", ment[0].id
#	sleep(5)

class Listener(tweepy.StreamListener):
    def on_data(self, data):
        print ((json.loads(data))['text']).encode('UTF-8'), '\n\n-----------\n\n'
        return True

    def on_error(self, status):
        print status

l = Listener()
auth = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
##auth.secure = True
auth.set_access_token(access_token2, access_token_secret2)

stream = tweepy.Stream(auth, l)
stream.filter(track=['basketball'])
#api.update_status('twapi post test')
