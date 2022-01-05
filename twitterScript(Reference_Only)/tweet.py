import tweepy
import random
from datetime import date
from datetime import datetime

names = [op.MAIN.op.COIN_DATA.op('NICK_1').text, op.MAIN.op.COIN_DATA.op('NICK_2').text, op.MAIN.op.COIN_DATA.op('NICK_3').text,op.MAIN.op.COIN_DATA.op('NICK_4').text, op.MAIN.op.COIN_DATA.op('NICK_5').text, op.MAIN.op.COIN_DATA.op('NICK_6').text,op.MAIN.op.COIN_DATA.op('NICK_7').text, op.MAIN.op.COIN_DATA.op('NICK_8').text, op.MAIN.op.COIN_DATA.op('NICK_9').text, op.MAIN.op.COIN_DATA.op('NICK_10').text]

auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

#Login
def oauth_login(API_KEY, SECRET_KEY):
    auth = tweepy.OAuthHandler(API_KEY, SECRET_KEY)
    auth_url = auth.get_authorization_url()
    verify_code = input("%s Verify Credentials: " % auth_url)
    print('Logging In')
    auth.get_access_token(verify_code)
    
    return tweepy.API(auth)

#Tweet_Script
def tweet():
#Parsing Text from Top Coins
	text = ["#" + name for name in names]
	
	tags = ['#CRYPTO', '#PYTHON', '#CRYPTOCOINS', '#CRYPTOCURRENCIES']
	
	finaltextList = ' '.join(text)
	finaltagsList = ' '.join(random.sample(tags,3))

#Calender Date
	
	today = str(date.today())
	time = datetime.now()
	current_time = time.strftime("%I:%M:%S %p")
	finalTweet = ("DATE: " + today + "\n" + "TIME: " + current_time + "\n" + "\n" + "RANKINGS: " + finaltextList + "\n" + "\n" + finaltagsList)
	print(finalTweet)
	
#Initializing Video	
	uploadDaily = api.media_upload(
    filename = r'\media\DAILY_UPLOAD.mov', chunked = True,
    media_category = "TweetVideo"
	)
	videoID = [uploadDaily.media_id_string]
	
#Constructing Tweet
	constructTweet = api.update_status(
		 media_ids = videoID, status = finalTweet
	)
	constructTweet
	print('Tweet Successful!')
	
tweet()
