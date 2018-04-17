# birb

![birb](images/birb.png)

birb is a minimalist app that lets you tweet from your CLI. No timeline, no search, no mentions: only posting.

## But why?

Twitter is noisy, and even a quick post can end up being distracting with your timeline and mentions popping up.
birb is limited on purpose so you don't fall into that waste of time: post now from your CLI, and mess with the rest later on.

## Usage

(usage example with screencast)

```sh
Usage: birb.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  oops   delete your most recent tweet
  tweet  send a tweet
```

Using the app without any command or parameter automatically triggers the `tweet` command.
You can delete your most recent tweet with `birb oops` if needed.
Be aware that this will delete your tweet regardless of where or when it has been posted.

If you want to repost right away, `birb oops --resend` will trigger the `tweet` command after deletion.

## Compatibility

birb has only been tested for Linux, and works with any version of Python3.
The main modules that birb depends on are `click` and `TwitterAPI`, which are installed automatically.

## Installation

Create an app on [apps.twitter.com](https://apps.twitter.com) with a name of your liking, and run `pip`:

```sh
pip install --user birb
```

You will be prompted to copy/paste the consumer keys and access tokens of the app you just created.
Those credentials will be locally stored at the top of `birb.py` and nowhere else, so you can interact with your application.

You're all set. Enjoy!

## Todo

* tweet threads
* tweet with media files