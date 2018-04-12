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
    r = api.request('statuses/user_timeline', {'count': 1})
    tweet_id = [False if 'ida' not in item else item['id'] for item in r]
    try:
        if tweet_id[0]:
            return tweet_id[0]
        else:
            raise Exception(tweet_id)
    except Exception:
        print(colors.FAIL + 
              'Stopping: tweet id not found. Status code returned: ' + 
              str(r.status_code) + colors.ENDC)

# optionally repost another tweet if supplied
def delete_last_tweet():
    tweet_id = get_last_tweet_id()
    r = api.request('statuses/destroy/:' + tweet_id)
    print(colors.FAIL + 'Last tweet deleted' + colors.ENDC
          if r.status_code == 200 
          else colors.FAIL + 'Error: ' + r.text + colors.ENDC)

# send a tweet with an image
def image():
    pass

get_last_tweet_id()