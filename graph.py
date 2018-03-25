import matplotlib.pyplot as plt
import numpy as np
from math import log

def best_fit(X, Y):
    # func pulled from https://stackoverflow.com/questions/22239691/code-for-line-of-best-fit-of-a-scatter-plot-in-python
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    return a, b

def graphDecisionPlane(p):
    pass

if __name__ == "__main__":
    
    x = np.arange(10)

    x = [5,10,50,100,200,1000]

    # Full results
    # y1 = [ 0.3117154811715481, 0.4602510460251046, 0.6527196652719666, 0.6820083682008368, 0.8326359832635983, 0.895397489539749]
    # y2 = [ 0.2928870292887029, 0.4686192468619247, 0.6234309623430963, 0.5983263598326359, 0.8138075313807531, 0.8891213389121339]
    # y3 = [0.44142259414225943, 0.3702928870292887, 0.6317991631799164,0.6569037656903766, 0.8765690376569037, 0.893305439330544]
    # y4 = [ 0.2907949790794979, 0.47280334728033474, 0.6171548117154811, 0.6861924686192469, 0.8619246861924686, 0.895397489539749]
    # y5 = [ 0.4456066945606695, 0.4895397489539749, 0.5711297071129707, 0.6652719665271967, 0.8577405857740585, 0.899581589958159]
    
    #Stemmed results 
    y1 = [ 0.5899581589958159, 0.6150627615062761, 0.5355648535564853, 0.606694560669456, 0.8661087866108786, 0.9246861924686193]
    y2 = [ 0.5209205020920502,  0.6799163179916318, 0.7573221757322176,  0.7907949790794979, 0.8410041841004184, 0.9079497907949791]
    y3 = [0.5230125523012552, 0.5983263598326359, 0.7280334728033473, 0.7510460251046025, 0.8514644351464435, 0.9079497907949791]
    y4 = [ 0.5230125523012552, 0.5125523012552301, 0.7740585774058577, 0.799163179916318, 0.8326359832635983, 0.9163179916317992]
    y5 = [ 0.4686192468619247, 0.604602510460251, 0.7384937238493724 , 0.7928870292887029, 0.803347280334728, 0.9163179916317992]

    lx = [log(xi,10) for xi in x]

    a, b = best_fit(lx, y1)
    y1fit = [a + b * xi for xi in lx]
    a, b = best_fit(lx, y2)
    y2fit = [a + b * xi for xi in lx]
    a, b = best_fit(lx, y3)
    y3fit = [a + b * xi for xi in lx]
    a, b = best_fit(lx, y4)
    y4fit = [a + b * xi for xi in lx]
    a, b = best_fit(lx, y5)
    y5fit = [a + b * xi for xi in lx]

    plt.scatter(lx, y1)
    plt.plot(lx,y1fit)
    plt.scatter(lx, y2)
    plt.plot(lx,y2fit)
    plt.scatter(lx, y3)
    plt.plot(lx,y3fit)
    plt.scatter(lx, y4)
    plt.plot(lx,y4fit)
    plt.scatter(lx, y5)
    plt.plot(lx,y5fit)

    plt.legend(['y1 = .01', 'y2 = .05', 'y3 = .1', 'y4 = .2', 'y5 = .3'], loc='upper left')
    plt.xlabel('Log10(Epoches)')
    plt.ylabel('Accuracy'),
    plt.savefig('graphResults.png')


