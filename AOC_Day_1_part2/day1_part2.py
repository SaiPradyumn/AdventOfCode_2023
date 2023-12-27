def getsum(line):
    numMap = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
    for key in numMap:
        if key in line:
            line = line.replace(key, numMap[key])
            #print("key : " + key + "value : " + numMap[key] )

    digit1 = 0
    digit2 = 0

    for x in line:
        if x.isdigit():
            if digit1 == 0:
                digit1 = int(x)
            digit2 = int(x)
    print(line + "--" + str(digit1) + "--" + str(digit2))
    return digit1*10 + digit2

if __name__ == '__main__':
    file = open("input_1.txt", "r")
    answer = 0
    for line in file:
        answer += getsum(line)
        #break

    print(answer)
