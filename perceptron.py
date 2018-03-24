class Perceptron():

    def __init__(self, learningRate, featureVectorIn={}):
        #Since we need to correlate weights and inputs to specific words, we will use a dict for the weights instead of a vector
        self.featureVector = featureVectorIn # dict
        self.weightVector = {} # dict
        self.n = learningRate

    # Don't need to explicitly set, set while training
    #def initFeatures(self,trainedBoW):
    #    self.featureVector = trainedBoW
    #    self.featureVector["THRESHOLD"] = 1 # setting a W0 bias
    #def initWeights(self):
        #initialize weights to size of input vector, init to 0 instead of random
    #    self.weightVector = {x:0 for x in featureVector.keys()}

    def classify(self, inputDict):
        #given an input attr dict from a test email, classify it 
        wxArr = []
        for key in inputDict.keys():
            wxArr.append(featureVector[key]*weightVector[key])
        res = sum(wxArr)
        return 1 if res >1 else 0
           
    def train(self, target, dir):
        '''(int, dict) -> None
            Takes in target (class value, so 1 for ham and 0 for spam) and
            directory of the training emails. Then it goes through each email,
            creates a bag of words for that email, and trains the perceptron 
            using the training rule wi <- wi + delta(wi), where delta(wi) 
            = n(t-o)xi. n is learning rate, (t-o) is the difference between
            perceptron output and target value, and xi is the specific attr
            we are updating the weight wi for
        '''
        for doc in os.listdir(dir):
            stemmedDoc = stemDoc(dir+doc)
            bag = initBagFromList(stemmedDoc)
            for key,value in bag.items():
                if key in self.featureVector:
                    # w inc by 1
                else:
                    # add entry in fV, set w to 1
                
        pass

    def initBagFromList(doclist):
        ''' (list) -> dict

            Given the name of a stemmed list (doclist) generated from 
            a single email, convert the document into a bag of 
            words stored as a dictionary and return the bag.
        '''
        d = {}
        for word in doclist:
            if not word in d:
                d[word] = 1
            else:
                d[word] += 1
        return d

    def initBagFromFile(st):
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
