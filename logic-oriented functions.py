def IsAllUnique(List):
    SetOfSeenThings=set()
    for index in range(len(List)):
        if List[index] in SetOfSeenThings:
            return False
        SetOfSeenThings.add(List[index])
    return True
    
def NumOfSimilaritiesAndMatchesToCase(List,Case):#returns as (Similarities,Matches)
    Similarities=0
    Matches=0
    for index in range(len(List)):
        if str(List[index])==str(Case):#Match
            Matches+=1
        elif str(Case) in str(List[index]):#Similarity
            Similarities+=1
    return Similarities,Matches
    
def RemoveDuplicates(numList):
    if len(numList)<=1:
        return numList
    Mid=len(numList)//2
    Left=RemoveDuplicates(numList[:Mid])
    Right=RemoveDuplicates(numList[Mid:])
    LeftComparisonIndex=0
    while len(Left)>0 and len(Right)>0 and LeftComparisonIndex<len(Left):
        for RightIndex in range(len(Right)-1,-1,-1):
            if Left[LeftComparisonIndex]==Right[RightIndex]:
                Right.pop(RightIndex)
        LeftComparisonIndex+=1
    return Left+Right
