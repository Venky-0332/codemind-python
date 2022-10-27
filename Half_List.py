n=int(input())
l=list(map(int,input().split()))
m=n//2
a=l[:m]
b=l[m:]
c=b[::-1] + l[:m]
print(*c)