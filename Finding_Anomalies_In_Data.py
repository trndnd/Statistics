def FindingAnomaly(NumbersList):
    Sorted_NumbersList = NumbersList.sort()
    InterQuartileRange = Sorted_NumbersList[-1] - Sorted_NumbersList[0]
    LowerQuartile,UpperQuartile = LowerAnUpperQuartile(NumbersList)
    LowerBound = LowerQuartile - 1.5(InterQuartileRange)
    UpperBound = UpperQuartile - 1.5(InterQuartileRange)
    AnomaliesArray = []
    for number in NumbersList:
        if number < LowerBound or number > UpperBound:
            AnomaliesArray.append(number)

def LowerAnUpperQuartile(NumbersList):
    NumberListLength = len(NumbersList)
    if NumberListLength % 2 == 0:
        LowerQuartile,UpperQuartile = LowerQuartileAndUpperQuartileForEvenLists(NumbersList)
    else:
        LowerQuartile,UpperQuartile = LowerQuartileAndUpperQuartileForOddLists(NumbersList)
    return LowerQuartile,UpperQuartile

def LowerQuartileAndUpperQuartileForOddLists(NumbersList):
    NumberListLength = len(NumbersList) - 1 #We do this not becuase of math but because of the indexing of lists
    MedianIndexValue =  (NumberListLength) / 2
    LowerQuartileList = NumbersList[:int(MedianIndexValue)]
    UpperQuartileList = NumbersList[int(MedianIndexValue + 1):]
    if len(LowerQuartileList) % 2 == 0:
        LowerQuartile = FindingMedianOfAListEven(LowerQuartileList)
    else:
        LowerQuartile = FindingMedianOfAListOdd(LowerQuartileList)
    if len(UpperQuartileList) % 2 == 0:
        UpperQuartile = FindingMedianOfAListEven(UpperQuartileList)
    else:
        UpperQuartile = FindingMedianOfAListOdd(UpperQuartileList)
    return LowerQuartile,UpperQuartile

def LowerQuartileAndUpperQuartileForEvenLists(NumbersList):
    NumbersListLength = len(NumbersList) # Lower it by one as lists/arrays start at 0 so a 8 long list would be still 7 numbers long but it would just at 0 and end at 7
    MiddleIndexValue = int(round(NumbersListLength / 2,0)) # Not actaully the middle but jjust about in the middle to be able to split the array into two arrays
    LowerQuartileList = NumbersList[:MiddleIndexValue]
    UpperQuartileList = NumbersList[MiddleIndexValue:]
    if len(LowerQuartileList) % 2 == 0:
        LowerQuartile = FindingMedianOfAListEven(LowerQuartileList)
    else:
        LowerQuartile = FindingMedianOfAListOdd(LowerQuartileList)
    if len(UpperQuartileList) % 2 == 0:
        UpperQuartile = FindingMedianOfAListEven(UpperQuartileList)
    else:
        UpperQuartile = FindingMedianOfAListOdd(UpperQuartileList)
    return LowerQuartile,UpperQuartile
    
def FindingMedianOfAListEven(NumbersList):#Finds the mean of 2 values in the middle to find the median
    MedianLowerValueIndex = int((len(NumbersList) - 1) / 2)
    MedianUpperValueIndex = int(((len(NumbersList) - 1) / 2) + 1)
    MedianValue = (NumbersList[MedianLowerValueIndex] + NumbersList[MedianUpperValueIndex]) / 2
    return MedianValue

def FindingMedianOfAListOdd(NumbersList):
    MedianIndexValue = int((len(NumbersList) - 1)/2)
    return NumbersList[MedianIndexValue]

#print(LowerQuartileAndUpperQuartileForEvenLists([3,6,7,10,19,23,26,29,32,37]))
print(LowerQuartileAndUpperQuartileForEvenLists([3,6,7,8,9,10]))
print(LowerQuartileAndUpperQuartileForOddLists([10,12,16,19,23]))