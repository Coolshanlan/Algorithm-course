import csv
import time
import datetime
import random
import matplotlib.pyplot as plt


def inputSplit(inp):
    opList = []
    numberList = []
    number = ""
    for i in inp:
        if i == "+" or i == "*":
            opList.append(i)
            numberList.append(int(number))
            number = ""
        elif i == "-":
            if number == "":
                number = "-"
            else:
                opList.append(i)
                numberList.append(int(number))
                number = ""
        else:
            number = number + i
    numberList.append(int(number))
    return numberList, opList


def computeNumber(numberList, opList):  # 用不到  (+-*多項式計算)
    stack = []
    for i in range(len(numberList)):
        if i != 0 and stack[-1] == "*":
            num1 = numberList[i]
            stack.pop()
            num2 = stack.pop()
            stack.append(num1*num2)
        elif i != len(numberList)-1:
            stack.append(numberList[i])
            stack.append(opList[i])
        else:
            stack.append(numberList[i])
    count = len(stack)//2
    for i in range(count):
        num1 = stack.pop()
        op = stack.pop()
        num2 = stack.pop()
        value = (num1+num2) if op == "+" else ((num1-num2)
                                               if op == "-" else (num2 * num1))
        stack.append(value)
    return stack.pop()


def traditionR(numberList, opList):
    value_max = -99999
    value_min = 99999
    if len(opList) == 1:
        return eval(str(numberList[0])+opList[0]+str(numberList[1])), eval(str(numberList[0])+opList[0]+str(numberList[1]))
    else:
        for i in range(len(opList)):
            num1Min = 0
            num2Min = 0
            num1Max = 0
            num2Max = 0
            op = opList[i]
            if i == 0:
                num1Max = numberList[0]
            else:
                num1Max, num1Min = traditionR(numberList[:i+1], opList[:i])
            if i == len(opList)-1:
                num2Max = numberList[i+1]
                num2Min = numberList[i+1]
            else:
                num2Max, num2Min = traditionR(numberList[i+1:], opList[i+1:])
            value_max = max(eval(str(num1Max)+op+str(num2Max)), value_max)
            value_min = min(value_max, value_min)
            value_max = max(eval(str(num1Max)+op+str(num2Min)), value_max)
            value_min = min(value_max, value_min)
    return value_max, value_min


def DP(numberList, opList):
    dp = [[0]*len(numberList) for i in range(len(numberList))]
    step = [[""]*len(numberList) for i in range(len(numberList))]

    for i in range(0, len(numberList)):
        dp[i][i] = numberList[i]
        step[i][i] = str(numberList[i])
    for i in range(1, len(numberList)):
        for j in range(0, len(numberList)-i):
            dp[j][j+i] = -99999
            dp[j+i][j] = 99999
            for k in range(0, i):
                op = opList[k+j]
                num1 = dp[j][j+k]
                num2 = dp[j+k+1][i+j]
                num2_min = dp[i+j][j+k+1]
                value = (num1+num2) if op == "+" else ((num1-num2)
                                                       if op == "-" else (num2 * num1))
                valuemin = (num1+num2_min) if op == "+" else ((num1-num2_min)
                                                              if op == "-" else (num2_min * num1))
                maxvalue = max(value, valuemin)
                minvalue = min(value, valuemin)
                if dp[j][i+j] < maxvalue:
                    dp[j][j+i] = maxvalue
                    step[j][j+i] = "("+step[j][j+k]+op+step[j+k+1][i+j]+")"
                if dp[i+j][j] > minvalue:
                    dp[i+j][j] = minvalue
                    step[i+j][j] = "("+step[j][j+k]+op+step[j+k+1][i+j]+")"
    return dp[0][len(numberList)-1], step[0][len(numberList)-1][1:-1]


inp = input("input:")

numberList, opList = inputSplit(inp)
dp_value, step = DP(numberList, opList)
print(step)
# time
# numberList = []
# opList = []
# epoch = 17
# numberList.append(2)

# for i in range(epoch):
#     numberList.append(random.randrange(10))
#     rndo = random.randrange(3)
#     op = "+" if rndo == 0 else "-" if rndo == 1 else"*"
#     opList.append(op)
# Dptime = []
# Traditime = []
# for i in range(epoch):
#     print(i)
#     starttime = time.time()
#     DP(numberList[:i+2], opList[:i+1])
#     endtime = time.time()
#     cost = str((endtime - starttime))[:5]
#     Dptime.append(cost)
#     print("DPtime:"+str(cost))
#     starttime = time.time()
#     traditionR(numberList[:i+2], opList[:i+1])
#     endtime = time.time()
#     cost = str((endtime - starttime))[:5]
#     Traditime.append(cost)
#     print("Trantime:"+str(cost))
#     # plt.plot(y, Dptime)
#     # plt.plot(y, Traditime)
#     # plt.title("PyPlot First Example")
#     # plt.pause(0.1)
# with open('log.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(Dptime)
#     writer.writerow(Traditime)
# print(Dptime, Traditime)
