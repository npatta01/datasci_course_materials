import sys
import json
from collections import OrderedDict

frequency = {}
total_tags=0

def computeFrequency(tweet_file):
    """ For the given file, compute relative frequency for a word"""
    global total_num_words
    global total_tags
    for tweet in tweet_file: # for a given tweet
        j_tweet=json.loads(tweet.encode('utf-8'))# parse the  tweet
        if ("entities" in j_tweet
            and len(j_tweet["entities"]["hashtags"])!=0):

            tags=j_tweet["entities"]["hashtags"];

            for t in tags:
                tag=t["text"].encode('utf-8')
                frequency[tag]=frequency.get(tag,0)+1
                total_tags+=1
                
            

def printTopK(topk=10):
    global total_tags
    l=OrderedDict(sorted(frequency.items(), key=lambda t: t[1],reverse=True))

    for (elem,elemvalue) in l.iteritems():
        if (topk!=0):
            print "%s\t%f" % (elem, elemvalue/total_tags)
            topk=topk-1;
    
        
def main():
    tweet_file = open(sys.argv[1]) #file that contains score of words
    computeFrequency(tweet_file)
    printTopK(10)

if __name__ == '__main__':
    main()
