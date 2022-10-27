n=int(input())
m=int(input())
s=0
for i in range(n):
    l=list(map(int,input().split()))
    for j in l:
        s+=j
print(s)