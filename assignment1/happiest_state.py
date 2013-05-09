import sys
import json

sentimentDictionary = {}
tweetsentiment__by_state={}
us_state_abr=set();
def parseSentimentDictionary(sent_file):
    """ For the given file,save the score of each word"""
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        sentimentDictionary[term] = int(score)  # Convert the score to an integer.

def assignScores(tweet_file):
    """ For the given file, print the score of each tweet"""
    for tweet in tweet_file: # for a given tweet
        j_tweet=json.loads(tweet.encode('utf-8'))# parse the  tweet
        if ("text" in j_tweet):
            if ("place" in j_tweet and j_tweet["place"]  ) :# if tweet has text
                t_Text= j_tweet["text"].encode('utf-8'); # get text of tweet
                assert isinstance(t_Text,str);
                words_in_tweet= t_Text.split();# get words in tweet
        
                # get the score of tweet based on sentiment dictionary
                total_Score=0.0;
                for w in words_in_tweet:
                    if(w in sentimentDictionary):
                        total_Score+=sentimentDictionary[w]

                place_dict=j_tweet["place"]
            
                if (place_dict["country_code"]=="US"):
                   us_state=place_dict["name"]

                   places=place_dict["full_name"].split()

                   us_state=None
                   for p in places:
                       p=p.strip()
                       if p in us_state_abr:
                        us_state=p


                   if ( us_state):
                       if (us_state in tweetsentiment__by_state):
                           u=tweetsentiment__by_state[us_state]
                           u.total_score+=total_Score
                           u.num_tweets+=1
                           
                       else:
                            u = StateSentiment()
                            u.total_score=total_Score
                            u.state=us_state
                            tweetsentiment__by_state[us_state]=u
                   
                   
def happiestState():
    hs =  StateSentiment()
    hs.total_score=-sys.maxint
    for value in tweetsentiment__by_state.itervalues():
        assert isinstance(value,StateSentiment)

        if value.total_score >hs.total_score:
            hs=value;


    print hs.state                                 
           
        

def createStateAbbrevation():
    global us_state_abr
    us_state_abr.add("AL")
    us_state_abr.add("AK")
    us_state_abr.add("AZ")
    us_state_abr.add("AR")
    us_state_abr.add("CA")
    us_state_abr.add("CO")
    us_state_abr.add("CT")
    us_state_abr.add("DE")
    us_state_abr.add("DC")
    us_state_abr.add("FL")
    us_state_abr.add("GA")
    us_state_abr.add("HI")
    us_state_abr.add("ID")
    us_state_abr.add("IL")
    us_state_abr.add("IN")
    us_state_abr.add("IA")
    us_state_abr.add("KS")
    us_state_abr.add("KY")
    us_state_abr.add("LA")
    us_state_abr.add("ME")
    us_state_abr.add("MT")
    us_state_abr.add("NE")
    us_state_abr.add("NV")
    us_state_abr.add("NH")
    us_state_abr.add("NJ")
    us_state_abr.add("NM")
    us_state_abr.add("NY")
    us_state_abr.add("NC")
    us_state_abr.add("ND")
    us_state_abr.add("OH")
    us_state_abr.add("OK")
    us_state_abr.add("OR")
    us_state_abr.add("MD")
    us_state_abr.add("MA")
    us_state_abr.add("MI")
    us_state_abr.add("MN")
    us_state_abr.add("MS")
    us_state_abr.add("MO")
    us_state_abr.add("PA")
    us_state_abr.add("RI")
    us_state_abr.add("SC")
    us_state_abr.add("SD")
    us_state_abr.add("TN")
    us_state_abr.add("TX")
    us_state_abr.add("UT")
    us_state_abr.add("VT")
    us_state_abr.add("VA")
    us_state_abr.add("WA")
    us_state_abr.add("WV")
    us_state_abr.add("WI")
    us_state_abr.add("WY")



class StateSentiment:
    state=""
    num_tweets=1
    total_score=0

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sentiment_file = open(sys.argv[1],"r") #file that contains score of words
    tweet_file = open(sys.argv[2])  #file that contains tweets
    #convert word/score to dictionary
    parseSentimentDictionary(sentiment_file) 
    createStateAbbrevation()
    assignScores(tweet_file)
    happiestState()


if __name__ == '__main__':
    main()
