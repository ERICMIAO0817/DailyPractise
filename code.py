"""
http://118.190.20.162/view.page?gpid=T153
ccfcsp 202209-1
"""
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = []
c = 1
tc = 1
temp = 0
for i in a:
    tc = i*tc
    b.append((m%tc-temp)//c)
    c = tc
print(*b)