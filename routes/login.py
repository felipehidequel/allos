from flask import Blueprint, redirect, render_template, request
import tweepy
import os
import dotenv
from database.db import SESSION

login_route = Blueprint('login', __name__)

callback = 'http://allos.com/login'

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACESS_TOKEN')
access_token_secret = os.getenv('ACESS_TOKEN_SECRET')

@login_route.route('/auth')
def auth():
    global SESSION
    oauth1_user_handler = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret, callback)
    url = oauth1_user_handler.get_authorization_url(signin_with_twitter=True)
    SESSION['request_token'] = oauth1_user_handler.request_token
    return redirect(url)

@login_route.route('/login')
def login():
    global SESSION
    request_token = SESSION['request_token']
    del SESSION['request_token']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    auth.request_token = request_token
    verifier = request.args.get('oauth_verifier')
    auth.get_access_token(verifier)
    SESSION['token'] = (auth.access_token, auth.access_token_secret)

    return redirect('/new')


@login_route.route('/new')
def app_route():
    global SESSION
    access_token, access_token_secret = SESSION['token']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    user = api.verify_credentials()
    
    return render_template('user.html', user=user)