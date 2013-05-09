import sys
import json

frequency = {}
total_num_words=0

def computeFrequency(tweet_file):
    """ For the given file, compute relative frequency for a word"""
    global total_num_words
    for tweet in tweet_file: # for a given tweet
        j_tweet=json.loads(tweet.encode('utf-8'))# parse the  tweet
        if ("text" in j_tweet) :# if tweet has text
            t_Text= j_tweet["text"].encode('utf-8'); # get text of tweet
            assert isinstance(t_Text,str);
            words_in_tweet= t_Text.split();# get words in tweet
        
            # for each word in tweet
            for w in words_in_tweet:
                total_num_words+=1 #increment total words
                #increment freq of w
                frequency[w]=frequency.get(w,0)+1
                
            

def printFinalFrequency():
    global total_num_words
    for w in frequency:
        freq=float(frequency[w])
        print "%s\t%f" % (w, freq/total_num_words)
        
def main():
    tweet_file = open(sys.argv[1]) #file that contains score of words
    computeFrequency(tweet_file)
    printFinalFrequency()

if __name__ == '__main__':
    main()
