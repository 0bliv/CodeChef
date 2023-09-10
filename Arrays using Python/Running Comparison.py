t = int(input())

for _ in range(t):
    n = int(input())
    
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    count = sum(1 for i in range(n) if arr1[i] <= 2 * arr2[i] and arr2[i] <= 2 * arr1[i])
    
    print(count)
