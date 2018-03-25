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


if __name__ == "__main__":
    
    x = np.arange(10)

    x = [5,10,50,100,200,1000]

    y1 = [ 0.3117154811715481, 0.4602510460251046, 0.6527196652719666, 0.6820083682008368, 0.8326359832635983, 0.895397489539749]
    y2 = [ 0.2928870292887029, 0.4686192468619247, 0.6234309623430963, 0.5983263598326359, 0.8138075313807531, 0.8891213389121339]
    y3 = [0.44142259414225943, 0.3702928870292887, 0.6317991631799164,0.6569037656903766, 0.8765690376569037, 0.893305439330544]
    y4 = [ 0.2907949790794979, 0.47280334728033474, 0.6171548117154811, 0.6861924686192469, 0.8619246861924686, 0.895397489539749]
    y5 = [ 0.4456066945606695, 0.4895397489539749, 0.5711297071129707, 0.6652719665271967, 0.8577405857740585, 0.899581589958159]

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


