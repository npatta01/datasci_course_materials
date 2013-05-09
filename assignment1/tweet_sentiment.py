import sys
import json

sentimentDictionary = {}


def parseSentimentDictionary(sent_file):
    """ For the given file,save the score of each word"""
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        sentimentDictionary[term] = int(score)  # Convert the score to an integer.

def assignScores(tweet_file):
    """ For the given file, print the score of each tweet"""
    for tweet in tweet_file: # for a given tweet
        j_tweet=json.loads(tweet.encode('utf-8'))# parse the  tweet
        if ("text" in j_tweet) :# if tweet has text
            t_Text= j_tweet["text"].encode('utf-8'); # get text of tweet
            assert isinstance(t_Text,str);
            words_in_tweet= t_Text.split();# get words in tweet
        
            # get the score of tweet based on sentiment dictionary
            total_Score=0.0;
            for w in words_in_tweet:
                if(w in sentimentDictionary):
                    total_Score+=sentimentDictionary[w]

            print total_Score
        


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sentiment_file = open(sys.argv[1],"r") #file that contains score of words
    tweet_file = open(sys.argv[2])  #file that contains tweets
    #convert word/score to dictionary
    parseSentimentDictionary(sentiment_file) 
    assignScores(tweet_file)


if __name__ == '__main__':
    main()
