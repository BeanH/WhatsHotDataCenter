
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


#ret =twitter.search.tweets(q= '%2349ers',result_type = 'popular')
#print json.dumps(ret)
###########examples of api usage##########

#iterator = twitter_stream.statuses.sample()   # Get a sample of the public data following through Twitter
#twitter.search.tweets(q='#nlproc')
world_trends = twitter.trends.available(_woeid=1)  #what trends are available worldwide
#sfo_trends = twitter.trends.place(_id = 2487956)     # get trends by location code
#results = twitter.users.search(q = '"New Cross"')   # user search
#query = twitter.search.tweets(q= "%2349ers",result_type = "popular")
#print json.dumps(world_trends)


countrys = {}
woeid = []
for tweet in world_trends:

    countryName = tweet.get('country')
    locations = countrys.get(countryName)
    woeid.append(tweet.get('woeid'))
    if(locations != None):
        locations.append(tweet.get('name'))
        countrys[countryName] = locations
    else:
        newSet = [tweet.get('name')]
        countrys[countryName] = newSet


with open('results.txt','w') as file:
    for location in woeid:
        tweets = twitter.trends.place(_id = location)
        #print json.dumps(tweets)
        trends = tweets[0]['trends']  # trendings
        store_entity = {}
        store_entity["woeid"]= location
        store_entity["locationName"]= tweets[0]["locations"][0]["name"]

        for trending in trends:
            query = trending.get("query")
            store_entity["hashtag"]= query
            popular_tweets = twitter.search.tweets(q= query,result_type = "popular",count = 5)
            statuses = popular_tweets.get("statuses")
            count = 3
            top_3_status = []
            for status in statuses:
                if count<=0:
                    break;
                map = {}
                map["text"] = status.get("text")
                map["favorite_count"] = status["favorite_count"]
                map["retweet_count"] = status["retweet_count"]
                top_3_status.append(map)

            store_entity["top_tweets"] = top_3_status
            json.dump(store_entity,file)
        #todo write into DB






#-----------------------------------------------------------------------
# perform the API query
# twitter API docs: https://dev.twitter.com/rest/reference/get/friendships/show
#-----------------------------------------------------------------------
#result = twitter.friendships.show(source_screen_name = source,
#   target_screen_name = target)#

#-----------------------------------------------------------------------
# extract the relevant properties
#-----------------------------------------------------------------------
# following = result["relationship"]["target"]["following"]
# follows   = result["relationship"]["target"]["followed_by"]

# print("%s following %s: %s" % (source, target, follows))
# print("%s following %s: %s" % (target, source, following))
