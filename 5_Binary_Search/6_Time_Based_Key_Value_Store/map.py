from collections import defaultdict

timeMap = defaultdict(list)
timeMap["alice"].append(["happy", 1])
timeMap["alice"].append(["happy", 7])
timeMap["alice"].append(["sad", 5])
timeMap["alice"].append(["sad", 10])
timeMap["alice"].append(["sad", 3])
copy = sorted(timeMap["alice"], key=lambda item: item[1])
print(timeMap, len(timeMap["alice"]), sep="\n", end="\n\n")
print(copy, len(copy), sep="\n")