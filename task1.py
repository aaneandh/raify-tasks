inputText = open("input.txt", "r")

resultDict = dict()

for line in inputText:
	line = line.strip()
	line = line.lower()
	words = line.split(" ")
	for word in words:
		if word in resultDict:
			resultDict[word] = resultDict[word] + 1
		else:
			resultDict[word] = 1

for key in list(resultDict.keys()):
	print(key, ":", resultDict[key])