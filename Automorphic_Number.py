n=int(input())
n_l=len(str(n))
s_n=n**2
l_d=s_n%pow(10,n_l)
if l_d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")