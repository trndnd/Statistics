from Binomial_Formula_Interval import Interval_Probability
from TryingToGraph import GraphingBinomialDistributions

class Graphing():

    def GettingXValues(nValue):
        xArray = []
        for x in range(nValue + 1):
            xArray.append(x)
        return xArray
    
    def GettingValues(x):
        nValue = int(input("What is the n value? "))
        pValue = float(input("What is teh p value? "))
        qValue = 1 - pValue
        Interval = [0,nValue]
        Probabilities = Interval_Probability.IntervalProbabilityInAArray(Interval,nValue,pValue)
        xArray = Graphing.GettingXValues(nValue)
        Graphing.ActuallyGraphing(xArray,Probabilities)

    def ActuallyGraphing(xArray,Probabilities):
        GraphingBinomialDistributions.Graphing("",xArray,Probabilities)


a = Graphing()
a.GettingValues()  


