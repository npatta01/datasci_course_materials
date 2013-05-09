import sys
import json

sentimentDictionary = {}#contains the sentiment
unknown_words_score={}#unknown word score


def parseSentimentDictionary(sent_file):
    """ For the given file,save the score of each word"""
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        sentimentDictionary[term] = int(score)  # Convert the score to an integer.

def calculateFinalScores():
    """ For each term, print the final score
        final_score (t) = total_neg_score(t)/total_neg_count(t) +
                          total_pos_score(t)/total_pos_count(t)
    """
    for w in unknown_words_score:
        ob=unknown_words_score[w];
        assert isinstance(ob,UnknownWord)
        
        final_score=0.0
        #to check not dividing by zero
        #setting the score based on pos and neg
        if(ob.neg_sum>0):
            final_score+=(ob.neg_sum/ob.neg_count)
        elif (ob.pos_sum>0):
            final_score+=(ob.pos_sum/ob.pos_count)
        ob.final_score =final_score
        print "%s\t%f" % (ob.term, float(final_score))

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
                if(w in sentimentDictionary):
                    total_Score+=sentimentDictionary[w]
                else:
                    unknown_words.append(w)

            #for each unkown word
            pos_count=neg_count=pos_sum=neg_sum=0;
            
            #set the pos/neg cout to 1, if tweet was positive or negative
            if total_Score >=0 :
                pos_count+=1;
                pos_sum+=total_Score
            else:
                neg_count+=1
                neg_sum+=total_Score

            for w in unknown_words:#increment the values for unknown words
                if w in unknown_words_score:#if word was seen in another tweet
                    uw = unknown_words_score[w];
                    assert isinstance(uw,UnknownWord)
                    uw.neg_count+=neg_count
                    uw.neg_sum+=neg_sum
                    uw.pos_sum+=pos_sum
                    uw.pos_count+=pos_count
                else:#word not seen
                    uw=UnknownWord()
                    uw.term=w
                    uw.pos_count=pos_count
                    uw.neg_count=neg_count
                    uw.pos_sum = pos_sum
                    uw.neg_sum = neg_sum
                    unknown_words_score[w]=uw


class UnknownWord:
    """ A struct to represent some infomration
    for words that were not in the sampl 
    dictionary file"""
    term=""
    pos_count=0
    neg_count=0
    pos_sum=0.0
    neg_sum=0.0
    final_score=0.0


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
