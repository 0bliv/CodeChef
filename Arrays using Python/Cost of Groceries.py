# Function to calculate the total cost of groceries
def calculate_total_cost(N, X, freshness_values, cost_values):
    total_cost = 0
    for i in range(N):
        if freshness_values[i] >= X:
            total_cost += cost_values[i]
    return total_cost

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input the number of items and the minimum freshness value
    N, X = map(int, input().split())
    
    # Input the freshness values and cost values as arrays
    freshness_values = list(map(int, input().split()))
    cost_values = list(map(int, input().split()))
    
    # Calculate and print the total cost
    total_cost = calculate_total_cost(N, X, freshness_values, cost_values)
    print(total_cost)
