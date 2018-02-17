import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "GJ9rGKq3rtcYbpjZekjpF9Rdp",
    "consumer_secret"     : "gCw6Uw3cdmT0f3ZMfQ7fnAGWa4TfmgSKPIsip5dhoH0ue2Tcl4",
    "access_token"        : "964880385418170368-i4QlatvbHQDVThJwnrcEmRieBN9ywX3",
    "access_token_secret" : "JjrTjNZop5RwQUXoqB7U0nlcOsw7unqpGb7uRInj6VlIG"
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()