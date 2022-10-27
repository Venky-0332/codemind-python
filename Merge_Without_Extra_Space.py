n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    l1=list(map(int,input().split()))
    s=sorted(l+l1)
    print(*s)