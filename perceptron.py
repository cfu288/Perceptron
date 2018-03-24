class Perceptron():

    # Since we need to correlate weights and inputs to specific words, 
    # we will use a dict for the weights instead of a vector
    def __init__(self, learningRate, featureVectorIn={}):
        self.featureVector = featureVectorIn # dict
        self.weightVector = {} # dict
        self.n = learningRate

    # Need to init perceptron with set of attributes and their freq from ALL of the emails (spam and ham)
    def initFeatures(self,trainedBoW):
        self.featureVector = trainedBoW
        self.featureVector["BIAS"] = 1 # setting a W0 bias
    
    # Initialize weights to size of input vector, init to 0 instead of random
    def initWeights(self):
        self.weightVector = {x:0 for x in featureVector.keys()}

    #given an input attr dict from a test email, classify it 
    def classify(self, inputDict):
        wxArr = []
        for key in inputDict.keys():
            wxArr.append(featureVector[key]*weightVector[key])
        res = sum(wxArr)
        return 1 if res >1 else 0
           
    def train(self, target, inputDict):
        '''(int, dict) -> None
            Trains the perceptron on a new single email, provided as an inputDict.

            Takes in target (class value, so 1 for ham and 0 for spam) and
            dictionary of a single training email and trains the perceptron 
            using the training rule wi <- wi + delta(wi), where delta(wi) 
            = n(t-o)xi. n is learning rate, (t-o) is the difference between
            perceptron c(vector(X)) output and target value, and xi is the specific attr
            we are updating the weight wi for.
        '''
        o = classify(inputDict) # pre-calc, doesn't change per email
        for key in inputDict.keys():
            try:
                deltaWI = self.n * ( target - o ) * featureVector[key]
                weightVector[key] += deltaWI
            except KeyError as e:
                #key not found? Should not happen since Perceptron attr are set before training
                print("KEY {} not found".format(e))            
        
        #for doc in os.listdir(dir):
        #    stemmedDoc = stemDoc(dir+doc)
        #    bag = initBagFromList(stemmedDoc)
        #    for key,value in bag.items():
        #        if key in self.featureVector:
                    # w inc by 1
        #        else:
                    # add entry in fV, set w to 1
