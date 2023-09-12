T = int(input()) 

for _ in range(T):
    N = int(input()) 
    temperatures = list(map(int, input().split()))  
    min_value = min(temperatures)
    temperatures = [x for x in temperatures if x != min_value]
    print(min(temperatures))
    

