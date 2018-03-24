import perceptron
import argparse, os

def getArgs():
    p = argparse.ArgumentParser(
            description='Perceptron')
    p.add_argument('ham', 
            help='An already stemmed text file containing all of the \
            words in all the HAM emails in the TRAINING set')
    p.add_argument('spam', 
            help='An already stemmed text file containing all of the words \
            in all the SPAM emails in the TRAINING set')

def initBag(st):
    ''' (string) -> dict

        Given the name of a stemmed text file (st) generated from 
        all of the st files, convert the document into a bag of 
        words stored as a dictionary and return the bag
    '''
    d = {}
    with open(st,'r') as openFile:
        for line in openFile:
            for word in line.split():
                if not word in d:
                    d[word] = 1
                else:
                    d[word] += 1
    return d


if __name__ == "__main__":
    args = getArgs()
    ham = args.ham
    spam = args.spam

    hamBag = initBag(ham) # class 1
    spamBag = initBag(spam) # class 0

    p = Perceptron(.1)
    
