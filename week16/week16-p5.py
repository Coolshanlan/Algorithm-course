s_num = int(input("input the number of S set element :"))
S = input("input elements(1 3 5....) :").split(" ")
S = [int(i) for i in S]
M = int(input("input the M of the subset of sum :"))
s_sum = sum(S)
dp = [0 for i in range(0, M+1)]
# S.insert(0, 0)
dp[0] = 1
for e in range(0, len(S)):
    for i in range(M, 0, -1):
        if i < S[e]:
            break
        if(dp[i] or dp[i - S[e]]):
            dp[i] = 1

if dp[M] == 1:
    v = M
    elementindex = len(S)-1
    subset = []
    while(v != 0):
        if S[elementindex] <= v and dp[v-S[elementindex]] == 1:
            subset.append(S[elementindex])
            v = v-S[elementindex]
        elementindex -= 1
    print("Exist")
    print(subset)
else:
    print(f"Not exist any subset that sum of subset equal {M}")
