from scipy.integrate import quad
import numpy
import math 

def Denisty_Function(x):
    Numerator = numpy.exp(-(x**2/2))
    Denominator = math.sqrt(2 * math.pi)
    return Numerator/Denominator

def Finding_pvalue(Test_Statistic):
    if Test_Statistic < 0:#We do this as w
        Test_Statistic *= -1
    p_Value = quad(Denisty_Function,Test_Statistic,1000)
    return float(p_Value[0])

def Finding_Test_Statistic(Sample_Prortion_Of_Success,Population_Proportion_Of_Success,Population_Proportion_Of_Failure,Sample_Size):
    Numerator = (Sample_Prortion_Of_Success - Population_Proportion_Of_Success)
    Denominator = (math.sqrt((Population_Proportion_Of_Success * Population_Proportion_Of_Failure)/Sample_Size))
    Test_Statistic = Numerator/Denominator
    return Test_Statistic

def Hypothesis_Testing():
    print("What is the sample proportion of success?")
    Sample_Propotion_Of_Success = float(input("p̂ =  "))
    print("What is the population proprtion of success? ")
    Population_Proportion_Of_Success = float(input("p = "))
    Population_Propotion_Of_Failure = 1 - Population_Proportion_Of_Success
    print("What is the significance value? ")
    Significance_Value = float(input("α = "))
    print("What is the sample size? ")
    Sample_Size = int(input("n = "))
    Test_Stat = Finding_Test_Statistic(Sample_Propotion_Of_Success,Population_Proportion_Of_Success,Population_Propotion_Of_Failure,Sample_Size)
    P_Value = Finding_pvalue(Test_Stat)
    if P_Value < Significance_Value:
        print("We can reject the null hypothesis so the claim is true")
    else:
        print("We fail to reject the null hypothsis so the claim is not proven.")
        
Hypothesis_Testing()