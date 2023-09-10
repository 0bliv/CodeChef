# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max1 = max(arr)
    max2 = max(value for value in arr if value < max1)

    max_sum = max1 + max2
    print(max_sum)
