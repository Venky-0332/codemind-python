def Ugly(n):
    l=[2,3,5]
    for i in l:
        while n%i==0:
            n=n/i
    return n==1
n=int(input())
    
if Ugly(n)==1:
    print('Ugly Number')
else:
    print('Not Ugly Number')
    