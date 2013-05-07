import urllib
import json

base_url="http://search.twitter.com/search.json?q=microsoft&page="


for page in xrange(1,10):
    response = urllib.urlopen(base_url+str(page));

    unicode_tweet=response.read().encode('utf-8');
    assert isinstance(unicode_tweet,str)

    tweet_page= json.loads(unicode_tweet)

    assert isinstance(tweet_page,dict);

    tweets=tweet_page["results"];

    assert isinstance(tweets,list);

    print("Page %s Tweets:\n" %(page));
    for index, item in enumerate(tweets):
            print ("Tweet %s : %s" %(index ,  item["text"].encode('utf-8')));



