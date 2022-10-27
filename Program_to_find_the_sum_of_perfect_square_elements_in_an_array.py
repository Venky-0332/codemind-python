import math
n=int(input())
l=list(map(int,input().split()))
summ=0
for i in l:
    if math.sqrt(i)==int(math.sqrt(i)):
        summ+=i
print(summ)