import sys
import json
from collections import OrderedDict
sentimentDictionary = {}#contains the sentiment
unknown_words_score={}#unknown word score

def parseSentimentDictionary(sent_file):
    for line in sent_file:
        term, score  = line.split("\t")  
        sentimentDictionary[term] = int(score)  

def calculateFinalScores():
    for w in unknown_words_score:
        ob=unknown_words_score[w];
        assert isinstance(ob,UnknownWord)
        final_score=pos_score=neg_score=0.0
        if(ob.neg_count!=0):
            neg_score=(ob.neg_sum/ob.neg_count)
        if (ob.pos_count!=0):
            pos_score=(ob.pos_sum/ob.pos_count)

        t_count=float(ob.pos_count+ob.neg_count)
        final_score=(pos_score *(ob.pos_count/t_count)) + (neg_score *(ob.neg_count/t_count))
        ob.final_score =final_score

    l=OrderedDict(sorted(unknown_words_score.items(), key=lambda t: t[1].final_score,reverse=True))

    for (elem,elemvalue) in l.iteritems():
        print "%s\t%f" % (elem, float(elemvalue.final_score))

def cleanupWord(w):
    w=w.lower();
    if (len(w)==0): return w
    while( len(w)!=0 and ( w[-1]==';' or   w[-1]== ',' or  w[-1]=='.' or w[-1]=='\''  or w[-1]=='\"' or w[-1]=='?')):
        w=w[0:-1]
    while( len(w)!=0 and ( w[0]==';' or   w[0]== ',' or  w[0]=='.' or w[0]=='\''  or w[0]=='\"')):
        w=w[1:]
    return w
        
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
            unknown_words=[];
            for w in words_in_tweet:
                #w=cleanupWord(w)
                if len(w)!=0: 
                    if(w in sentimentDictionary):
                        total_Score+=sentimentDictionary[w]
                    else:
                        unknown_words.append(w)

            pos_count=neg_count=pos_sum=neg_sum=0
            if total_Score >=0 :
                pos_count=1;
                pos_sum=total_Score
            else :
                neg_count=1
                neg_sum=total_Score

            for w in unknown_words:#increment the values for unknown words
                if w in unknown_words_score:#if word was seen in another tweet
                    uw = unknown_words_score[w];
                    assert isinstance(uw,UnknownWord)
                    uw.neg_count=uw.neg_count+neg_count
                    uw.neg_sum=uw.neg_sum+neg_sum
                    uw.pos_sum=uw.pos_sum+pos_sum
                    uw.pos_count=uw.pos_count+pos_count
                else:#word not seen
                    uw=UnknownWord()
                    uw.term=w
                    uw.pos_count=pos_count
                    uw.neg_count=neg_count
                    uw.pos_sum = pos_sum
                    uw.neg_sum = neg_sum
                    unknown_words_score[w]=uw


class UnknownWord:
    term=""
    pos_count=neg_count=0
    pos_sum=neg_sum=final_score=0.0

def main():
    #sentiment file
    sent_file = open(sys.argv[1])
    #file containign tweets
    tweet_file = open(sys.argv[2])
    #parse word/score
    parseSentimentDictionary(sent_file)
    #count occurences,pos/neg score
    assignScores(tweet_file)
    #print score
    calculateFinalScores()


if __name__ == '__main__':
    main()