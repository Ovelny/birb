from TwitterAPI import TwitterAPI
from secrets import api
import click

# handle colors for terminal
class colors:
    PROCESSING = '\033[95m' + '[~] '
    OKBLUE = '\033[94m' + '[+] '
    OKGREEN = '\033[92m' + '[+] '
    WARNING = '\033[93m' + '[!] '
    FAIL = '\033[91m' + '[-] '
    ENDC = '\033[0m'


def print_help():
    pass

def parse_tweet(tweet, tweet_length):
    return False if len(tweet) > tweet_length else True

def birb():
    tweet_length = 280
    tweet = input(colors.PROCESSING + 'Compose your tweet: ' + colors.ENDC)
    if parse_tweet(tweet, tweet_length):
        r = api.request('statuses/update', {'status': tweet})
        print(colors.OKGREEN + 'Tweet sent!' + colors.ENDC 
              if r.status_code == 200 
              else colors.FAIL + 'Error: ' + r.text + colors.ENDC)
    else:
        print(colors.WARNING +
              'Your tweet is ', str(len(tweet) - tweet_length),
                 ' character(s) too long, please try again' +
              colors.ENDC)
        birb()

def get_last_tweet_id():
    pass

def delete_last_tweet():
    pass

# send a tweet with an image
def image():
    pass