
def printxstring(xindex):
    for i in range(len(str1)):
        if i == xindex:
            print("[", end='')
        print(str1[i], end='')
        if i == xindex:
            print("]", end='')


def printAllvariable(step, zvalue, dp):
    for i in range(len(str1)+1):
        print(step[i])
    for i in range(len(str1)+1):
        print(zvalue[i])
    for i in range(len(str1)+1):
        print(dp[i])


def printFinalSetp(step):
    zstring = ""
    xindex = 0
    zindex = 0
    for i in step[len(str1)][len(str2)]:
        if i == "1":
            zstring = zstring+str1[xindex]
            xindex += 1
            zindex += 1
            print("copy ", end='')
        elif i == "2":
            zstring = zstring + str1[xindex+1]+str1[xindex]
            xindex += 2
            zindex += 2
            print("twiddle ", end='')
        elif i == "3":
            zstring = zstring + str2[zindex]
            xindex += 1
            zindex += 1
            print("replace ", end='')
        elif i == "4":
            xindex += 1
            print("delete ", end='')
        elif i == "5":
            zstring = zstring + str2[zindex]
            zindex += 1
            print("insert ", end='')
        elif i == "6":
            zstring = zstring
            xindex = len(str1)+1
            print("kill ", end='')
        if i == "2":
            printxstring(xindex-2)
        else:
            printxstring(xindex - 1)
        print(" ", end='')
        print(zstring)


def editDistanceNoPath(str1, str2):
    costList = {"copy": 0,
                "replace": 1,
                "delete": 1,
                "insert": 1,
                "twiddle": 1,
                "kill": 0.5}
    dp = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(0, len(str2)+1):
        dp[0][i] = i
    for i in range(0, len(str1)+1):
        dp[i][0] = i

    for i in range(1, len(str1)+1):
        substr1 = str1[i-1]
        for j in range(1, len(str2)+1):
            substr2 = str2[j-1]
            c = costList["copy"] if substr1 == substr2 else costList["replace"]
            dp[i][j] = min(dp[i-1][j-1]+c, min(dp[i-1][j] +
                                               costList["delete"], dp[i][j-1]+costList["insert"]))
            if i > 1 and j > 1 and substr1 == str2[j-2] and substr2 == str1[i-2]:
                dp[i][j] = min(dp[i][j], dp[i-2][j-2]+costList["twiddle"])
    print("score:", end='')
    print(dp[len(str1)][len(str2)])


def editDistance(str1, str2):
    costList = {"copy": 0,
                "replace": 1,
                "delete": 1,
                "insert": 1,
                "twiddle": 1,
                "kill": 0.5}
    dp = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    step = [["" for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    stepNew = [["" for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    zvalue = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    for i in range(0, len(str2)+1):
        dp[0][i] = i
    for i in range(0, len(str1)+1):
        dp[i][0] = i
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
            if zvalue[i-1][j] == len(str2):
                zvalue[i][j] = zvalue[i-1][j]
                step[i][j] = step[i-1][j]
                nowmin = dp[i-1][j]-costList["kill"]
            if substr1 == substr2:
                if dp[i-1][j-1]+costList["copy"] <= nowmin:
                    zvalue[i][j] = zvalue[i-1][j-1]+1
                    step[i][j] = step[i-1][j-1]+"1"
                    stepNew[i][j] = "1"
                    nowmin = dp[i-1][j-1]+costList["copy"]
            if i > 1 and j > 1 and substr1 == str2[j-2] and substr2 == str1[i-2]:
                if dp[i-2][j-2]+costList["twiddle"] <= nowmin:
                    zvalue[i][j] = zvalue[i-2][j-2]+2
                    step[i][j] = step[i-2][j-2]+"2"
                    stepNew[i][j] = "2"
                    nowmin = dp[i-2][j-2]+costList["twiddle"]
            if substr1 != substr2:
                if dp[i-1][j-1]+costList["replace"] <= nowmin:
                    zvalue[i][j] = zvalue[i-1][j-1]+1
                    step[i][j] = step[i-1][j-1]+"3"
                    stepNew[i][j] = "3"
                    nowmin = dp[i-1][j-1]+costList["replace"]
            if dp[i-1][j]+costList["delete"] <= nowmin:
                zvalue[i][j] = zvalue[i-1][j]
                step[i][j] = step[i-1][j]+"4"
                stepNew[i][j] = "4"
                nowmin = dp[i-1][j]+costList["delete"]
            if dp[i][j-1]+costList["insert"] <= nowmin:
                zvalue[i][j] = zvalue[i][j-1]+1
                step[i][j] = step[i][j-1]+"5"
                stepNew[i][j] = "5"
                nowmin = dp[i][j-1]+costList["insert"]
            if zvalue[i][j] == len(str2) and i != len(str1) and step[i][j][-1] != "6":
                step[i][j] = step[i][j]+"6"
                stepNew[i][j] = stepNew[i][j]+"6"
            if step[i][j][-1] == "6":
                nowmin = nowmin+costList["kill"]
            dp[i][j] = nowmin
    print("score:", end='')
    print(dp[len(str1)][len(str2)])
    printFinalSetp(step)
    printAllvariable(step, zvalue, dp)


str1 = input("string 1 :")
str2 = input("string 2 :")
editDistance(str1, str2)
