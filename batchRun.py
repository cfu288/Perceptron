from hw3 import *

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

    #combos of epochs and learning rates
    COMBOS = [
    (5,.1),(10,.1),(50,.1),(100,.1),(200,.1),
    (5,.05),(10,.05),(50,.05),(100,.05),(200,.05),
    (5,.2),(10,.2),(50,.2),(100,.2),(200,.2),
    (5,.3),(10,.3),(50,.3),(100,.3),(200,.3),
    ]
    results = []

    i = 0
    for epoch,lr in COMBOS:
        i+=1
        print("{}/{}".format(i,len(COMBOS)), end="\r")


        p = Perceptron(lr)
        p.initFeatures(mergedBag)
        p.initWeights()
    
        for j in range(epoch):
            trainWithFiles(p, 1, trainHamDir)
            trainWithFiles(p, -1, trainSpamDir)
        
        hamTest = testWithFiles(p, 1, testHamDir)
        spamTest = testWithFiles(p, -1, testSpamDir)
        
        percCor = (hamTest[0]+spamTest[0])/(hamTest[1]+spamTest[1])
        
        results.append((epoch,lr,percCor))
    
    with open("results.txt", 'w') as outFile:
        for x,y,z in results:
            outFile.write("{} epoches with learning rate {} has {} correct\n".format(x,y,z))
