#!/usr/bin/python3
import copy

f = open("resources/dict.txt", "rt")
inputwords = f.readlines()
originalwords = [word.upper().strip() for word in inputwords]
words = [list(word.upper().strip()) for word in inputwords]

del inputwords

# Convert the words to numbers
for i in range(len(words)):
	for j in range(0, len(words[i])):
		ascii = ord(words[i][j])

		if ascii >= 65 and ascii <= 67:
			words[i][j] = "2"
		elif ascii >= 68 and ascii <= 69: 
			words[i][j] = "3"
		elif ascii >= 70 and ascii <= 73: 
			words[i][j] = "4"
		elif ascii >= 74 and ascii <= 76: 
			words[i][j] = "5"
		elif ascii >= 77 and ascii <= 79: 
			words[i][j] = "6"
		elif ascii >= 80 and ascii <= 83: 
			words[i][j] = "7"
		elif ascii >= 84 and ascii <= 86: 
			words[i][j] = "8"
		elif ascii >= 87: 
			words[i][j] = "9"

numbers = input("Enter Numbers for Prediction: ")

for i in range(len(numbers)):
	for j in range(len(words)):
		if i < len(words[j]):
			if words[j][i] != numbers[i]:
				originalwords[j] = ""

outputwords = [word for word in outputwords if word != ""]
print (outputwords)
