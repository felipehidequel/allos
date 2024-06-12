from flask import Blueprint, redirect, render_template
import tweepy
import os
import dotenv

login_route = Blueprint('login', __name__)

@login_route.route('/new')
def login_button():
    return render_template('login.html')

@login_route.route('/login', methods=['GET', 'POST'])
def login():
    dotenv.load_dotenv()
    redirect_url = '/login/success'
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    # access_token = os.getenv('ACESS_TOKEN')
    # access_token_secret = os.getenv('ACESS_TOKEN_SECRET')
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, redirect_url)
    redirect_url = auth.get_authorization_url()
    return redirect(redirect_url)