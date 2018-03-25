import random
class Perceptron():

    def __init__(self, learningRate):
        ''' (float) - > None
            Takes in a learning rate, inits a perceptron object. Since we need to 
            correlate weights and inputs to specific words, we will use a counter for 
            the weights instead of a vector
        '''
        self.featureVector = None # Will be Counter obj
        self.weightVector = None # counter
        self.n = learningRate

    def initFeatures(self,trainedBoW):
        ''' (Counter) -> None
            Init fV with passed in BoW counter of entire training set, adds a bias of 1 to fV
        '''
        self.featureVector = trainedBoW
        self.featureVector["__BIAS__"] = 1 # setting a W0 bias
        
    
    def initWeights(self):
        ''' (None) -> None
            Init wV to random values between-1 to 1 for each attr in fV
        '''
        self.weightVector = {x:random.uniform(-1,1) for x in self.featureVector.keys()}

    def classify(self, inputDict):
        ''' (Counter) -> int
            Provided a Bow from an individual email (as a Counter obj), classify whether
            it is of calss 1 or -1 given current perceptron training. Classify as 1 if
            linear combination of weights and attr is > 0, classify as -1 o/w.
        '''
        wxArr = []
        for key in inputDict.keys():
            try:
                wxArr.append(self.featureVector[key]*self.weightVector[key])
            except KeyError as e:
                # Note: KeyErrors should be normal during TESTING but not TRAINING
                pass
        wxArr.append(self.featureVector["__BIAS__"]*self.weightVector["__BIAS__"])
        res = sum(wxArr)
        return 1 if res>0 else -1
           
    def train(self, target, inputDict):
        '''(int, counter) -> None
            Trains the perceptron on a new single email, provided as an inputDict.

            Takes in target (class value, so 1 for ham and -1 for spam) and
            counter of a single training email and trains the perceptron 
            using the training rule wi <- wi + delta(wi), where delta(wi) 
            = n(t-o)xi. n is learning rate, (t-o) is the difference between
            perceptron c(vector(X)) output and target value, and xi is the specific attr
            we are updating the weight wi for.
        '''
        o = self.classify(inputDict) # pre-calc, c(vector(x)) doesn't change per email
        #Adjust Bias
        deltaWI = self.n * ( target - o ) * self.featureVector["__BIAS__"]
        self.weightVector["__BIAS__"] += deltaWI

        for key in inputDict.keys():
            try:
                deltaWI = self.n * ( target - o ) * self.featureVector[key]
                self.weightVector[key] += deltaWI
            except KeyError as e:
                #key not found? Should not happen since Perceptron attr are set before training
                #print("KEY {} not found".format(e))            
                pass 
