def getGameId_part1(line):
    words = line.split(" ")
    gameId = int(words[1].replace(":", ""))
    for i in range(3, len(words)):
        if "blue" in words[i] and int(words[i - 1]) > 14:
            return 0
        elif "green" in words[i] and int(words[i - 1]) > 13:
            return 0
        elif "red" in words[i] and int(words[i - 1]) > 12:
            return 0

    print("\n Game id success: " + str(gameId))
    return gameId


def getPowerSet(line):
    words = line.split(" ")
    gameId = int(words[1].replace(":", ""))
    minSet = [0, 0, 0]
    for i in range(3, len(words)):
        if "blue" in words[i]:
            if minSet[0] < int(words[i-1]):
                minSet[0] = int(words[i-1])
        elif "green" in words[i]:
            if minSet[1] < int(words[i-1]):
                minSet[1] = int(words[i-1])
        elif "red" in words[i]:
            if minSet[2] < int(words[i-1]):
                minSet[2] = int(words[i-1])

    powerset = minSet[1]*minSet[2]*minSet[0]
    print(str(gameId)+ ": " + str(minSet) + "--" + str(powerset))
    return powerset


if __name__ == '__main__':
    file = open("input_2.txt", "r")
    answer = 0
    for line in file:
        answer += getPowerSet(line)

    print(answer)
