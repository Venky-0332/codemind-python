n=int(input())
l=list(map(int,input().split()))
s=sorted(set(l))
a=len(set(l))
if a==2:
    print(max(l))
elif a==1:
    print(l[0])
else:
    print(s[-3])