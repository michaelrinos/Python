import tweepy, time, sys

#Twitter application info
CONSUMER_KEY = "XXX"
CONSUMER_SECRET = "XXX"
ACCESS_KEY = "XXX"
ACCESS_SECRET = "XXX"

#Connecting the bot to twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

query = "chance to win"
searched_tweets = []
last_id = -1
max_tweets = 1
while len(searched_tweets)<max_tweets:
	count = max_tweets-len(searched_tweets)
	try:
		new_tweets = api.search(q= query, count = 1, max_id = str(last_id-1))
		if not new_tweets:
			break
		searched_tweets.extend(new_tweets)
		last_id = new_tweets[-1].id
	except tweepy.TweepError as e:
		break
for i in new_tweets:
	print("This is the original text: "+i.text)
	print(i.user.id)
	y = i.text[i.text.find('@')+1:i.text.find(':',i.text.find('@'),len(i.text))]
	print("This is the original user: " + y)
	results = api.search_users(y)
	timeline = api.user_timeline(results)
	for tweet in timeline:
		print tweet.text
	
	
