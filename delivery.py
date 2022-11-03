"""
http://118.190.20.162/view.page?gpid=T153
ccfcsp 202209-2
"""
n, x = map(int,input().split())
a = []
dp = [0]*(n*x)
cost = []
for i in range(n):
    t = int(input())
    a.append(t)
pre = sum(a)
for i in range(n):
    for j in range(pre,a[i]-1,-1):
        dp[j] = max(dp[j],dp[j-a[i]]+a[i])
for i in range(x,pre+1):
    if dp[i]>=x:
        print(dp[i])
        break


    # for i in range(n):
#     goods.append([int(i) for i in input().split()])
# print(goods)

# dp = [0 for i in range(v + 1)]
#
# for i in range(n):
#     for j in range(v, -1, -1):  # 从后往前
#         if j >= goods[i][0]:
#             dp[j] = max(dp[j], dp[j - goods[i][0]] + goods[i][1])
#
# print(dp[-1])
