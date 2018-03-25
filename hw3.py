from perceptron import Perceptron
from nltk.stem.porter import *
from stemmer import stemDoc
from collections import Counter
import argparse, os, re, time

def getArgs():
    p = argparse.ArgumentParser(
            description='Perceptron')
    p.add_argument('ham', 
            help='An already stemmed text file containing all of the \
            words in all the HAM emails in the TRAINING set')
    p.add_argument('spam', 
            help='An already stemmed text file containing all of the words \
            in all the SPAM emails in the TRAINING set')
    p.add_argument('trainHamDir', 
            help='The directory where all the HAM emails in the TEST set \
                    are located')
    p.add_argument('trainSpamDir', 
            help='The directory where all the SPAM emails in the TEST set \
            are located')
    p.add_argument('testHamDir', 
            help='The directory where all the HAM emails in the TEST set \
                    are located')
    p.add_argument('testSpamDir', 
            help='The directory where all the SPAM emails in the TEST set \
            are located')
    p.add_argument('stopWords',nargs='?',default ='', 
            help='(optional) file of stopwords to ignore when stemming')
    return p.parse_args()

def initBagFromList(docList):
    ''' (list) -> Counter

        Given the name of a stemmed list (doclist) generated from 
        a single email, convert the document into a bag of 
        words stored as a counter and return the bag.
    '''
    return Counter(docList)

def initBagFromFile(st):
    ''' (string) -> Counter

        Given the name of a stemmed text file (st) generated from 
        all of the st files, convert the document into a bag of 
        words stored as a Counter and return the bag
    '''
    d = {}
    c = Counter()
    with open(st,'r') as openFile:
        for line in openFile:
            l = line.split()
            c.update(l)
    return c

def trainWithFiles(p, target, dir, stopwords="", cache=0, prevFiles=None):
    ''' (perceptron object, int, string) -> None
        
        Given an perceptron object and a directory path where the emails are, train
        the perceptron with emails. Target is 1 if emails are ham, -1 if they are spam.
        ** to save time in future epoch's, modified to save bags to a ds to access later.
        ** uses more memory but takes less time from i/o and memory allocation
    '''
    if prevFiles == None and cache==1:
        newL = []
        for doc in os.listdir(dir):
            stemmedDoc = stemDoc(dir+doc,stopwords)
            bag = initBagFromList(stemmedDoc)
            newL.append(bag)
            p.train(target,bag)
        return newL
    elif cache == 0:
        for doc in os.listdir(dir):
            stemmedDoc = stemDoc(dir+doc,stopwords)
            bag = initBagFromList(stemmedDoc)
            p.train(target,bag)
    else:
        for bag in prevFiles:
            p.train(target,bag)

def testWithFiles(p, target, dir, stopwords=""):
    total = 0
    numCorrect = 0
    for doc in os.listdir(dir):
        total += 1
        stemmedDoc = stemDoc(dir+doc,stopwords)
        bag = initBagFromList(stemmedDoc)
        ans =  p.classify(bag) 
        #print("{}=?={}".format(ans,target))
        if ans == target:
            numCorrect += 1
    #print("{} correct out of {}".format(numCorrect, total))        
    return (numCorrect,total)

if __name__ == "__main__":
    args = getArgs()
    ham = args.ham
    spam = args.spam
    trainHamDir = args.trainHamDir + '/' if (args.trainHamDir[-1] != '/') else args.trainHamDir
    trainSpamDir = args.trainSpamDir + '/' if (args.trainSpamDir[-1] != '/') else args.trainSpamDir
    testHamDir = args.testHamDir + '/' if (args.testHamDir[-1] != '/') else args.testHamDir
    testSpamDir = args.testSpamDir + '/' if (args.testSpamDir[-1] != '/') else args.testSpamDir
    stopWords = args.stopWords
    
    start = time.time()
    
    hamBag = initBagFromFile(ham) # class 1
    spamBag = initBagFromFile(spam) # class -1
    mergedBag = hamBag + spamBag

    p = Perceptron(.1)
    p.initFeatures(mergedBag)
    p.initWeights()
   
    cacheH = None
    cacheS = None
    epoch = 100
    print("TRAINING")
    for i in range(epoch):
        #Train with entire dataset
        print("{}/{}".format(i+1,epoch), end="\r")
        nCacheH = trainWithFiles(p, 1, trainHamDir, stopWords, 1, cacheH)
        nCacheS = trainWithFiles(p, -1, trainSpamDir, stopWords, 1, cacheS)
        cacheH = nCacheH if cacheH == None else cacheH
        cacheS = nCacheS if cacheS == None else cacheS
    print("TESTING")
    hamTest = testWithFiles(p, 1, testHamDir,stopWords)
    spamTest = testWithFiles(p, -1, testSpamDir,stopWords)
    print("PERCENT CORRECT {}".format((hamTest[0]+spamTest[0])/(hamTest[1]+spamTest[1])))
    
    print("Time Elapsed: {} seconds".format(time.time()-start))
