from perceptron import Perceptron
import argparse, os
from collections import Counter

def getArgs():
    p = argparse.ArgumentParser(
            description='Perceptron')
    p.add_argument('ham', 
            help='An already stemmed text file containing all of the \
            words in all the HAM emails in the TRAINING set')
    p.add_argument('spam', 
            help='An already stemmed text file containing all of the words \
            in all the SPAM emails in the TRAINING set')
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

def stemDoc(self, docPath,stopWords=""):
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

if __name__ == "__main__":
    args = getArgs()
    ham = args.ham
    spam = args.spam

    hamBag = initBagFromFile(ham) # class 1
    spamBag = initBagFromFile(spam) # class 0
    mergedBag = hamBag + spamBag

    print(hamBag)

    p = Perceptron(.1)
    
