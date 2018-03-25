from hw3 import *
import time

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
    (5,.01),(10,.01),(50,.01),(100,.01),(200,.01),
    (5,.1),(10,.1),(50,.1),(100,.1),(200,.1),
    (5,.05),(10,.05),(50,.05),(100,.05),(200,.05),
    (5,.2),(10,.2),(50,.2),(100,.2),(200,.2),
    (5,.3),(10,.3),(50,.3),(100,.3),(200,.3),
    (1000,.1),(1000,.05),(1000,.2),(1000,.3),(1000,.01),
    ]
    results = []

    start = time.time()
    with open("results.txt", 'a') as outFile:
        i = 0
        for epoch,lr in COMBOS:
            i+=1
            print("{}/{}".format(i,len(COMBOS)), end="\r")

            p = Perceptron(lr)
            p.initFeatures(mergedBag)
            p.initWeights()
            
            #Caching BoW for emails between epoches, saves time
            cacheH = None
            cacheS = None
            for j in range(epoch):
                nCacheH = trainWithFiles(p, 1, trainHamDir, stopWords,1,cacheH)
                nCacheS = trainWithFiles(p, -1, trainSpamDir, stopWords,1,cacheS)
                cacheH = nCacheH if cacheH == None else cacheH
                cacheS = nCacheS if cacheS == None else cacheS
            
            hamTest = testWithFiles(p, 1, testHamDir,stopWords)
            spamTest = testWithFiles(p, -1, testSpamDir,stopWords)
            
            percCor = (hamTest[0]+spamTest[0])/(hamTest[1]+spamTest[1])
            
            #results.append((epoch,lr,percCor))
        
            #for x,y,z in results:
            #write for each itr so something is saved if the proc is killed over ssh
            outFile.write("{} epoches with learning rate {} has {} correct\n".format(epoch,lr,percCor))
    print("Time Elapsed: {} seconds".format(time.time()-start))
