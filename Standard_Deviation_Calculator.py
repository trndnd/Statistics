import math as m
def Deviation_On_A_Sample(Numbers_Array):
    Sum_of_Difference = 0
    Mean = (sum(Numbers_Array))/len(Numbers_Array)
    for Number in Numbers_Array:
        Difference = Number - Mean
        Sum_of_Difference += (Difference**2)
    Standard_Deviation_Sample = m.sqrt((Sum_of_Difference)/(len(Numbers_Array) - 1))
    print(f"The sample deviation is {Standard_Deviation_Sample}")
    return Standard_Deviation_Sample

def Deviation_On_A_Population(Numbers_Array):
    Sum_of_Difference = 0
    Mean = (sum(Numbers_Array))/len(Numbers_Array)
    for Number in Numbers_Array:
        Difference = Number - Mean
        Sum_of_Difference += (Difference**2)
    Standard_Deviation_Population = m.sqrt((Sum_of_Difference)/len(Numbers_Array))
    print(f"The population deviation is {Standard_Deviation_Population}")

def Z_Score(dataValue,Mean,Standard_Deviation):
    ZScore = (dataValue - Mean)/Standard_Deviation
    return ZScore


SampleArray = [68, 73, 86, 72, 82, 78]
s = Deviation_On_A_Sample(SampleArray)
Deviation_On_A_Population(SampleArray)
#print(f"The data value is {Z_Score(4,3.2,s)} deviations away from the mean")