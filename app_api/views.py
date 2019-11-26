from django.shortcuts import render
from twython import Twython
import requests
from .helpers import *
import json

APP_KEY = 'YOUR_APP_KEY'
APP_SECRET = 'YOUR_SECRET_KEY'

'''
    Add your callback url into twitter app and here. Don't forget HTTPS.
'''
def index(request):
    twitter = Twython(APP_KEY, APP_SECRET)
    auth = twitter.get_authentication_tokens(callback_url='https://example.com/complete/twitter/')
    OAUTH_TOKEN = auth['oauth_token']
    OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
    OAUTH_URL = auth['auth_url']
    context = {
        'auth_url' : auth['auth_url']
    }

    return render(request, 'home.html', context)

def callback(request):
    oauth_verifier = request.GET['oauth_verifier']
    oauth_token = request.GET['oauth_token']
    twitter = Twython(APP_KEY, APP_SECRET,oauth_token, oauth_verifier)
    final_step = twitter.get_authorized_tokens(oauth_verifier)

    # Generate final token and secret and save them into db
    OAUTH_TOKEN = final_step['oauth_token']
    OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
    timeline = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    timeline.verify_credentials()
    screen_name = timeline.verify_credentials()["screen_name"]
    user_tweets = timeline.get_user_timeline(screen_name=screen_name, include_rts=True)

    # Get Messeges with help of custom function
    home_timeline = oauth_req('https://api.twitter.com/1.1/direct_messages/events/list.json', OAUTH_TOKEN, OAUTH_TOKEN_SECRET )
    
    data = json.loads(home_timeline)

    context = {
        'oauth_token': OAUTH_TOKEN,
        'token_secret': OAUTH_TOKEN_SECRET,
        'all_tweets': user_tweets,
        'all_messages': data,
    }
    return render(request, 'callback.html', context)