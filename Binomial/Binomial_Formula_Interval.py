import math
from Binomial_Formula import Binomial

class Interval_Probability():
    def IntervalProbabilityNormally(Interval,n,p):#like at most 3 where we want the probabilities of P(x = 0),P(x = 1),P(x = 2),P(x = 3)
        totalProbability = 0
        for num in range(Interval[0],Interval[-1] + 1):
            probability = Binomial.BinomialFormula(n,num,p)
            totalProbability += probability
        return totalProbability

    def AskingUsersForValues():
        nValue = int(input("What is the n value? "))
        pValue = float(input("What is your p value? "))
        StartingPosition = int(input("What is the number you want to start at? "))
        EndingPosition = int(input("What is the number you want to end at? "))
        Interval = [StartingPosition,EndingPosition]
        TotalProbability = Interval_Probability.IntervalProbabilityNormally(Interval,nValue,pValue)
        print(TotalProbability)
        print(f"The probability is around {round(TotalProbability * 100 ,2)}%")
        
a = Interval_Probability
a.AskingUsersForValues()