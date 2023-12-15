from apify_client import ApifyClient

class TweetAPI:

    def __init__(self, API_KEY):
        self.API_KEY = API_KEY

    def extract_text_from_twitter_link(self, tweet_url):
        # Initialize the ApifyClient with your API token
        client = ApifyClient(self.API_KEY)    
        
        run_input = {
            "startUrls": [{"url": tweet_url}],
            "tweetsDesired": 1,
            "addUserInfo": False,
        }

        run = client.actor("KVJr35xjTw2XyvMeK").call(run_input=run_input)

        # Fetch and return the full_text of the tweet
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            return item.get("full_text", None)