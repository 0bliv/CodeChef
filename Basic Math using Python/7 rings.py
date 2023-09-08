# cook your dish here

t = int(input())
for i in range (t):
    n,x = map(int,input().split())
    
    total = n*x
    
    if total <= 99999 and total >= 10000:
        print("YES")
    else:
        print("NO")