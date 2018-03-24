class Perceptron():

    def __init__(self, featureVectorIn={}):
        #Since we need to correlate weights and inputs to specific words, we will use a dict for the weights instead of a vector
        self.featureVector = featureVectorIn # dict
        self.weightVector = {} # dict

    def initFeatures(trainedBoW):
        self.featureVector = trainedBoW

    def initWeights():
        #initialize weights to size of input vector, init to .5 instead of random
        self.weightVector = {x:0.5 for x in featureVector.keys()}

    def classify(inputDict):
        #given an input attr dict from a test email, classify it 
        wxArr = []
        for key in inputDict.keys():
            wxArr.append(featureVector[key]*weightVector[key])
        res = sum(wxArr)
        return 1 if res >1 else 0
            
