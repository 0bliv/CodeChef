# cook your dish here
t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    resp = ((x*5)+(y*10))//z
    print(resp)
