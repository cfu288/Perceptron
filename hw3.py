from perceptron import Perceptron
from nltk.stem.porter import * 
from collections import Counter
import argparse, os, re

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

def stemDoc(docPath,stopWords=""):
    stopWordsL = []
    if stopWords != "":
        with open(stopWords,'r', encoding='utf-8', errors='ignore') as stopFile:
            for line in stopFile:
                for word in line.split():
                    stopWordsL.append(word.lower())
     
    unstemmed_words_list = []
    regex = re.compile('[^a-zA-Z0-9]')
    with open(docPath,'r',encoding='utf-8', errors='ignore') as openFile:
        for line in openFile:
            for word in line.split():
                if word not in stopWords:
                    cleaned = regex.sub('', word)
                    if len(cleaned) > 0:
                        unstemmed_words_list.append(cleaned.lower())
    stemmer = PorterStemmer()
    stemmed_words_list = [stemmer.stem(plural) for plural in unstemmed_words_list]
    return stemmed_words_list

def trainWithFiles(p, target, dir):
    ''' (perceptron object, string) -> None
        
        Given an perceptron object and a directory path where the emails are, train
        the perceptron with emails. Target is 1 if emails are ham, -1 if they are spam.
    '''
    for doc in os.listdir(dir):
        stemmedDoc = stemDoc(dir+doc)
        bag = initBagFromList(stemmedDoc)
        p.train(target,bag)

def testWithFiles(p, target, dir):
    total = 0
    numCorrect = 0
    for doc in os.listdir(dir):
        total += 1
        stemmedDoc = stemDoc(dir+doc)
        bag = initBagFromList(stemmedDoc)
        ans =  p.classify(bag) 
        #print("{}=?={}".format(ans,target))
        if ans == target:
            numCorrect += 1
    print("{} correct out of {}".format(numCorrect, total))        
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

    hamBag = initBagFromFile(ham) # class 1
    spamBag = initBagFromFile(spam) # class -1
    mergedBag = hamBag + spamBag

    p = Perceptron(.1)
    p.initFeatures(mergedBag)
    p.initWeights()

    print("------------TRAINING HAM------------")
    trainWithFiles(p, 1, trainHamDir)
    #print("\n----------TRAINING SPAM-----------")
    #trainWithFiles(p, -1, trainSpamDir)

    #print("\n------------TESTING HAM--------------")
    #hamTest = testWithFiles(p, 1, testHamDir)
    #print("\n-----------TESTING SPAM--------------")
    #spamTest = testWithFiles(p, -1, testSpamDir)
    #print("PERCENT CORRECT {}".format((hamTest[0]+spamTest[0])/(hamTest[1]+spamTest[1])))
