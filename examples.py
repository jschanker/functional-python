from fun import *

def existsEvenInList(numList):
	def isEven(num):
		return num % 2 == 0

	return existsItemIn(numList, isEven)

def hasWhiteSpace(word):
	def isWhiteSpace(letter):
		return letter == '\t' or letter == ' '

	return existsItemIn(word, isWhiteSpace)

def isEveryNumberPositiveIn(numberList):
	def isPositive(num):
		return num > 0

	return forEachItemIn(numberList, isPositive)

def isValidListOfScores(scores):
	def isValidScore(score):
		return score >= 0 and score <= 100

	return forEachItemIn(scores, isValidScore)

def hasPrime(numList):
	def isPrime(num):
		def notADivisor(d):
			return num % d != 0

		return forEachItemIn(range(2, num), notADivisor)

	return existsItemIn(numList, isPrime)

def hasAllAdditiveInverses(values):
	def hasAdditiveInverse(num):
		def equalToOpposite(num2):
			return num == -num2

		return existsItemIn(values, equalToOpposite)

	return forEachItemIn(values, hasAdditiveInverse)

def allPositiveEvens(numList):
	def positiveIsEven(num):
			return num <= 0 or num % 2 == 0

	return forEachItemIn(numList, positiveIsEven)

def allUniqueNumbers(values):
	def numAtIndexIsUnique(index1):
		def numNotEqualValueAtIndex(index2):
			return values[index1] != values[index2]

		return forEachIndexOf(values, numNotEqualValueAtIndex, index1)

	return forEachIndexOf(values, numAtIndexIsUnique)

print(allUniqueNumbers([4,1,3,4]))