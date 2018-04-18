#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TwitterAPI import TwitterAPI
#from birb_secrets import api
import click
#import os
api = None
'''if api is None:
    
    here = os.path.abspath(os.path.dirname(__file__))
    # Ask for twitter API keys
    print("Create an app on https://apps.twitter.com and paste the following infos to use birb: ")
    consumer_key = input("Paste consumer key here: ")
    consumer_secret = input("Paste consumer secret here: ")
    access_token_key = input("Paste access token here: ")
    access_token_secret = input("Paste access token secret here: ")

api = TwitterAPI('a','a','a','a')
                                    + '\'' + consumer_secret + '\'' + ','
                                    + '\'' + access_token_key + '\'' + ','
                                    + '\'' + access_token_secret + '\'' + ')\n')

    with open(os.path.join(here, 'birb_secrets.py'), 'r+', encoding='utf-8') as script:
        content = script.readlines()
        script.seek(0)
        for line in content:
api = TwitterAPI('a','a','a','a')
                script.write(line)
            else:
                script.write(credentials)
        script.truncate()
'''
@click.group(invoke_without_command=True)
@click.pass_context
def birb(context):
    if context.invoked_subcommand is None:
        tweet()

@birb.command('tweet', short_help='send a tweet')
def tweet():
    tweet_length = 280
    tweet = input(colors.PROCESSING + 'Compose your tweet: ' + colors.ENDC)
    if parse_tweet(tweet, tweet_length):
        r = api.request('statuses/update', {'status': tweet})
        print(colors.OKGREEN + 'Tweet sent! (°∋°)' + colors.ENDC 
              if r.status_code == 200 
              else colors.FAIL + 'Error: ' + r.text + colors.ENDC)
    else:
        print(colors.WARNING +
              'Your tweet is ' + str(len(tweet) - tweet_length) +
                 ' character(s) too long, please try again' +
              colors.ENDC)
        tweet()

@birb.command('oops', short_help='delete your most recent tweet')
@click.option('--resend', is_flag=True, help="resend a tweet immediately")
@click.pass_context
def delete_last_tweet(context, resend):
    tweet_id = get_last_tweet_id()
    r = api.request('statuses/destroy/:' + str(tweet_id))
    print(colors.FAIL + 'Last tweet deleted' + colors.ENDC
          if r.status_code == 200 
          else colors.FAIL + 'Error: ' + r.text + colors.ENDC)
    if resend:
        context.invoke(tweet)


# ------------
#  Helpers
# ------------

# handle colors for terminal
class colors:
    PROCESSING = '\033[95m' + '[~] '
    OKBLUE = '\033[94m' + '[+] '
    OKGREEN = '\033[92m' + '[+] '
    WARNING = '\033[93m' + '[!] '
    FAIL = '\033[91m' + '[-] '
    ENDC = '\033[0m'

def parse_tweet(tweet, tweet_length):
    return False if len(tweet) > tweet_length else True

def get_last_tweet_id():
    r = api.request('statuses/user_timeline', {'count': 1})
    tweet_id = [False if 'id' not in item else item['id'] for item in r]
    try:
        if tweet_id[0]:
            return tweet_id[0]
        else:
            raise Exception(tweet_id)
    except Exception:
        print(colors.FAIL + 
              'Stopping: tweet id not found. Status code returned: ' + 
              str(r.status_code) + colors.ENDC)


if __name__ == '__main__':
    birb()