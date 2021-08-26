import math
class FindingUsualValues():
    def __init__(self):
        nValue,pValue,qValue = FindingUsualValues.AskingForValues()
        Succusses = FindingUsualValues.ExpectedNumberOfSuccesses(nValue,pValue)
        Deviation = FindingUsualValues.StandardDeviaton(Succusses,qValue)
        LowerBound,UpperBound = FindingUsualValues.TwoStandardDeviations(Deviation,Succusses)
        UsualValues = FindingUsualValues.GettingUsualValues(Deviation,LowerBound,UpperBound)
        print(UsualValues)

    def AskingForValues():
        nValue = int(input("What is the n value? "))
        pValue = float(input("What is the p value? "))
        qValue = 1 - pValue
        return nValue,pValue,qValue

    def ExpectedNumberOfSuccesses(n,p):
        NumberOfSuccesses = float(n * p)
        return NumberOfSuccesses
    
    def StandardDeviaton(NumberofSuccesses,q):
        Deviation = math.sqrt(NumberofSuccesses * q)
        return Deviation

    def TwoStandardDeviations(Deviation,Succusses):
        TwoStandardDeviationsToTheRight = Succusses + (2 * Deviation)#Equal to µ - 2(σ)
        TwoStandardDeviationsToTheLeft = Succusses - (2 * Deviation)#Eual to µ + 2(σ)
        return TwoStandardDeviationsToTheLeft,TwoStandardDeviationsToTheRight
    
    def GettingUsualValues(Deviation,LowerBound,UpperBound):
        UsualValuesArray = []
        LowerBound = int(LowerBound + 1)#Not actually the lower bound at this point as we are using the lower bound to actually get the usual values
        UpperBound = int(UpperBound)
        x = LowerBound
        while x <= UpperBound:
            UsualValuesArray.append(x)
            x += 1
        return UsualValuesArray

a = FindingUsualValues()
