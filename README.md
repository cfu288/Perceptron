# Single Perceptron to Classify Ham/Spam emails

I used python to implement a Perceptron that can train on a set of HAM or SPAM emails and distinguish between new instances of HAM or SPAM emails after training.

Emails were first stemmed using the nltk porter stemmer, then converted into a bag of words (using python's Counter data structure). 

## Files:
* **hw3.py** is the driver code. It parses and formats incoming emails that are eventually passed to the perceptron object for either training ot testing. The main code defaults to 100 epoches and a .1 learning rate. To run hw3.py:

    * python3 hw3.py \[AllStemmedHam\] \[AllStemmedSpam\] \[trainHamDir\] \[trainSpamDir\] \[testHamDir\] \[testSpamDir\]
        * AllStemmedHam : an already stemmed text file containing all of the words in all the HAM emails in the TRAINING set
        * AllStemmedSpam : an already stemmed text file containing all of the words in all the SPAM emails in the TRAINING set
        * trainHamDir : The directory where all the HAM emails in the TEST set are located
        * trainSpamDir : The directory where all the SPAM emails in the TEST set are located
        * testHamDir : The directory where all the HAM emails in the TEST set are located
        * testSpamDir : The directory where all the SPAM emails in the TEST set are located

* Sample Command:
    * python3 hw3.py stemmedFiles/train-ham-stemmed.txt stemmedFiles/train-spam-stemmed.txt train/ham train/spam test/ham test/spam

* **perceptron.py** is a class that stores the perceptron data and functions. It takes in a learning rate upon initialization and is passed in pre-stemmed BagOfWords Counter objects (instead of a traditional vector - we need to map individual words to their attribute values during both training and testing time which a vector can't do but a counter can) for training and testing.
* **batchRun.py** takes the same arguments as above, but runs 20 combinations of Epoches and learning rates. Takes a while, I run this overnight.
* **graph.py** just generated a graph form my results.
* **stemmer.py** is the script used to stem a directory of emails or individual emails. To run on an entire directory (used to generate AllStemmedHam and AllStemmedSpam> for HW3.py)
    * python3 stemmer.py \[dirPath\] \[outFile\]
        * dirPath : path of directory you want to convert to a stemmed file
        * outfile : name/path of stemmed file

Results of perceptron tests are shown below, where I varied the learning rate (between .01 and .3) and number of epoches (between 5 and 1000):


![Accuracy of perceptron given different learning rates and epoches](results/graphResults.png)
