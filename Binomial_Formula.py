#nCx * p^x * q^(n-x)
import math
class Binomial():
    def CombinationFuncton(n,x):
        Combinations = (math.factorial(n))/(math.factorial(x) * math.factorial(n-x))#n!/((n-x)! * x!)
        return Combinations

    def BinomialFormula(n,x,p):#Finds the probability
        q = float(1 - p)
        temp = n - x
        Combinations = Binomial.CombinationFuncton(n,x)
        Probability = Combinations * (p**x) * (q**(temp))
        return Probability

    def AskingUserForValues():
        nValue = int(input("What is the n value? "))
        xValue = int(input("What is your x value? "))
        pValue = float(input("What is your p value? "))
        Probability = Binomial.BinomialFormula(nValue,xValue,pValue)
        print(Probability)
        print(f"It has around a {round(Probability * 100,2)}% chance of happening")

