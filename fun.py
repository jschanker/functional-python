def forEachItemIn(itemList, claim):
	trueForEveryItemInListSoFar = True
	for item in itemList:
		if(not(claim(item))):
			trueForEveryItemInListSoFar = False

	return trueForEveryItemInListSoFar

def forEachIndexOf(itemList, claim, excludingIndex=None):
	trueForEveryIndexInListSoFar = True
	for index in range(len(itemList)):
		if(excludingIndex != index and not(claim(index))):
			trueForEveryIndexInListSoFar = False

	return trueForEveryIndexInListSoFar

def existsItemIn(itemList, claim):
	foundItemInListYet = False
	for item in itemList:
		if(claim(item)):
			foundItemInListYet = True

	return foundItemInListYet