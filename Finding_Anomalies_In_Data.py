def FindingAnomaly(NumbersList):
    Sorted_NumbersList = NumbersList.sort()
    InterQuartileRange = Sorted_NumbersList[-1] - Sorted_NumbersList[0]
    LowerBound = 9
    UpperBound = float(1.5 * 9)

def LowerAnUpperQuartile(NumbersList):
    NumberList_Length = len(NumbersList)
    if NumberListLength % 2 == 0:
        LowerQuartileAndUpperQuartileForEvenLists(NumbersList,NumberList_Length)

def LowerQuartileAndUpperQuatrileForOddLists(NumbersList):
    NumberListLength = len(NumbersList) - 2 #We do this not becuase of math but because of the indexing of lists
    MedianIndexValue = (NumberListLength + 1) / 2
    LowerQuartileList = NumbersList[:int(MedianIndexValue)]
    UpperQuartileList = NumbersList[int(MedianIndexValue) + 1:]
    if len(LowerQuartileList) % 2 == 0:
        LowerQuartile = FindingMedianOfAListEven(LowerQuartileList)
    else:
        LowerQuartile = FindingMedianOfAListOdd(LowerQuartileList)
    if len(UpperQuartileList) % 2 == 0:
        UpperQuartile = FindingMedianOfAListEven(UpperQuartileList)
    else:
        UpperQuartile = FindingMedianOfAListOdd(UpperQuartileList)
    return LowerQuartile,UpperQuartile

def LowerQuartileAndUpperQuartileForEvenLists(NumbersList,NumberListLength):
    Numbe
    medianIndexNumber = round(NumberListLength/2,0)
    
def FindingMedianOfAListEven(NumbersList):
    MedianLowerValueIndex = int((len(NumbersList) - 1) / 2)
    MedianUpperValueIndex = int(((len(NumbersList) - 1) / 2) + 1)
    MedianValue = (NumbersList[MedianLowerValueIndex] + NumbersList[MedianUpperValueIndex]) / 2
    return MedianValue

def FindingMedianOfAListOdd(NumbersList):
    MedianIndexValue = int((len(NumbersList) - 1)/2)
    return NumbersList[MedianIndexValue]

print(LowerQuartileAndUpperQuatrileForOddLists([1,2,56,80,96,100,101]))