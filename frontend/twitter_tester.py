import unittest

from TweetAPI import TweetAPI

class Tester(unittest.TestCase):

    def test1(self):

        tweet_url = 'https://twitter.com/irctcrandom/status/1735631922918011005?t=K4D86e7-hWxlNxbcZiLJlA&s=19'
        tweet_txt = 'All posts in this account are part of testing a website.. Please ignore. No one is targeted.'
        
        tweet_api = TweetAPI(API_KEY='apify_api_2QGQH8DkI54nayPr5grpIauvPmWqFL3NwQ4M')
        api_tweet_txt = tweet_api.extract_text_from_twitter_link(tweet_url)

        self.assertEqual(tweet_txt, api_tweet_txt)
        print('\r', end = '')
        print(f"Expected --> {tweet_txt}, Predicted --> {api_tweet_txt}")



if __name__ == '__main__':

    unittest.main()