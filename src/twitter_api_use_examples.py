
import twitter
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
CONSUMER_KEY = 'cn9ESfxWeOtY3AYeB4WCNFPX0'
CONSUMER_SECRET = 'hB8Ya6tO822QcphmQlzBA13lVdzh2Ie8Jc8p9ZoYt6JP78uxYm'
ACCESS_TOKEN = '1046995753883881472-2NwQ173RDmv3XS7NP9irEDvho1atf6'
ACCESS_SECRET = 'MNwh5gCdEDWu3JfOfxakQqzVcc0rYIVYSA9hXhr3uW5nP'


oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter = Twitter(auth=oauth)


###########examples of api usage##########

#iterator = twitter_stream.statuses.sample()   # Get a sample of the public data following through Twitter
#twitter.search.tweets(q='#nlproc')
world_trends = twitter.trends.available(_woeid=1)  #what trends are available worldwide
#sfo_trends = twitter.trends.place(_id = 2487956)     # get trends by location code
#results = twitter.users.search(q = '"New Cross"')   # user search
#query = twitter.search.tweets(q = "pink elephants")
#statuses = twitter.statuses.home_timeline(count = 50)
#tweets = twitter.statuses.user_timeline(screen_name="49ersfangirl")
#followers = twitter.followers.ids(screen_name="cocoweixu")
#print followers
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
 tweet_count = 10
 for tweet in world_trends:
     tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
     print json.dumps(tweet)  
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    # if tweet_count <= 0:
        # break 
        # 
        # 
        # 
# source = "ideoforms"
# target = "lewisrichard"

#-----------------------------------------------------------------------
# perform the API query
# twitter API docs: https://dev.twitter.com/rest/reference/get/friendships/show
#-----------------------------------------------------------------------
#result = twitter.friendships.show(source_screen_name = source,
                                  target_screen_name = target)

#-----------------------------------------------------------------------
# extract the relevant properties
#-----------------------------------------------------------------------
# following = result["relationship"]["target"]["following"]
# follows   = result["relationship"]["target"]["followed_by"]

# print("%s following %s: %s" % (source, target, follows))
# print("%s following %s: %s" % (target, source, following))