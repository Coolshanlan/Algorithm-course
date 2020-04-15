import numpy as np


def printAllStep():
    for i in step[len(str1)][len(str2)]:
        if i == "1":
            print("+", end='')
        elif i == "2":
            print("-", end='')
        else:
            print("*", end='')


def printFinalSetp():
    zstring = ""
    xstring = ""
    xindex = 0
    zindex = 0
    for i in step[len(str1)][len(str2)]:
        if i == "1":
            xstring = xstring+str1[xindex]
            xindex += 1
        elif i == "2":
            xstring = xstring+str1[xindex]
            xindex += 1
        elif i == "3":
            xstring = xstring+str1[xindex]
            xindex += 1
        elif i == "4":
            xstring = xstring + " "
    print(xstring)
    for i in step[len(str1)][len(str2)]:
        if i == "1":
            zstring = zstring+str2[zindex]
            zindex += 1
        elif i == "2":
            zstring = zstring+str2[zindex]
            zindex += 1
        elif i == "3":
            zstring = zstring+" "
        elif i == "4":
            zstring = zstring+str2[zindex]
            zindex += 1
    print(zstring)


str1 = input("string 1 :")
str2 = input("string 2 :")
dp = [[1 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
costList = {"copy": -1,
            "replace": 2,
            "delete": 2,
            "insert": 2,
            "twiddle": 999999999,
            "kill": 99999999
            }
step = [["" for i in range(len(str2)+1)] for j in range(len(str1)+1)]
for i in range(0, len(str2)+1):
    dp[0][i] = i*costList["insert"]
for i in range(0, len(str1)+1):
    dp[i][0] = i*costList["delete"]

i = 0
j = 0

while i < len(str1):
    i += 1
    j = 0
    substr1 = str1[i-1]
    while j < len(str2):
        j += 1
        substr2 = str2[j-1]
        nowmin = 9999
        if substr1 == substr2:
            if dp[i-1][j-1]+costList["copy"] <= nowmin:
                step[i][j] = step[i-1][j-1]+"1"
                nowmin = dp[i-1][j-1]+costList["copy"]
        if substr1 != substr2:
            if dp[i-1][j-1]+costList["replace"] <= nowmin:
                step[i][j] = step[i-1][j-1]+"2"
                nowmin = dp[i-1][j-1]+costList["replace"]
        if dp[i-1][j]+costList["delete"] <= nowmin:
            step[i][j] = step[i-1][j]+"3"
            nowmin = dp[i-1][j]+costList["delete"]
        if dp[i][j-1]+costList["insert"] <= nowmin:
            step[i][j] = step[i][j-1]+"4"
            nowmin = dp[i][j-1]+costList["insert"]
        dp[i][j] = nowmin
print("score:", end='')
print(dp[len(str1)][len(str2)])
printFinalSetp()
printAllStep()
print("")
for i in range(len(str1)+1):
    print(dp[i])
for i in range(len(str1)+1):
    print(step[i])
