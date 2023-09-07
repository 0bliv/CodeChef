# cook your dish here
n=int(input())
for i in range(n):
    (x,y,a)=map(int,input().split())
    
    if a >= x and a < y:
        # TODO: write code...
        print("yes")
    
    else:
        print("no")