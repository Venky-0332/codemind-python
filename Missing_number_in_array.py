n=int(input())
for i in range(n):
    s=int(input())
    l=list(map(int,input().split()))
    for i in range(1,s+1):
        if i not in l:
            print(i)