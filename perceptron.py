from nltk.stem.porter import * 

class Perceptron():

    def __init__(self, learningRate, featureVectorIn={}):
        #Since we need to correlate weights and inputs to specific words, we will use a dict for the weights instead of a vector
        self.featureVector = featureVectorIn # dict
        self.weightVector = {} # dict
        self.n = learningRate

    def initFeatures(self,trainedBoW):
        self.featureVector = trainedBoW
        self.featureVector["THRESHOLD"] = 1 # setting a W0 bias

    def initWeights(self):
        #initialize weights to size of input vector, init to 0 instead of random
        self.weightVector = {x:0 for x in featureVector.keys()}

    def classify(self, inputDict):
        #given an input attr dict from a test email, classify it 
        wxArr = []
        for key in inputDict.keys():
            wxArr.append(featureVector[kdef stemDoc(docDir,stopWords=""):
    stopWordsL = []
    if stopWords != "":
        with open(stopWords,'r', encoding='utf-8', errors='ignore') as stopFile:
            for line in stopFile:
                for word in line.split():
                    stopWordsL.append(word.lower())
     
    unstemmed_words_list = []
    regex = re.compile('[^a-zA-Z0-9]')
    with open(docDir,'r',encoding='utf-8', errors='ignore') as openFile:
        for line in openFile:
            for word in line.split():
                if word not in stopWords:
                    cleaned = regex.sub('', word)
                    if len(cleaned) > 0:
                        unstemmed_words_list.append(cleaned.lower())
    #print(unstemmed_words_list)
    stemmer = PorterStemmer()
    stemmed_words_list = [stemmer.stem(plural) for plural in unstemmed_words_list]
 ey]*weightVector[key])
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
            
        pass

    def stemDoc(self, docDir,stopWords=""):
        stopWordsL = []
        if stopWords != "":
            with open(stopWords,'r', encoding='utf-8', errors='ignore') as stopFile:
                for line in stopFile:
                    for word in line.split():
                        stopWordsL.append(word.lower())
         
        unstemmed_words_list = []
        regex = re.compile('[^a-zA-Z0-9]')
        with open(docDir,'r',encoding='utf-8', errors='ignore') as openFile:
            for line in openFile:
                for word in line.split():
                    if word not in stopWords:
                        cleaned = regex.sub('', word)
                        if len(cleaned) > 0:
                            unstemmed_words_list.append(cleaned.lower())
        stemmer = PorterStemmer()
        stemmed_words_list = [stemmer.stem(plural) for plural in unstemmed_words_list]
        return stemmed_words_list
