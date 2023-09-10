# Function to check if the list is in non-decreasing order
def is_non_decreasing(difficulties):
    for i in range(1, len(difficulties)):
        if difficulties[i] < difficulties[i - 1]:
            return False
    return True

# Input the number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input the number of problems solved by the students
    N = int(input())
    
    # Input the difficulty ratings as a list
    difficulty_ratings = list(map(int, input().split()))
    
    # Check if the list is in non-decreasing order and print the result
    if is_non_decreasing(difficulty_ratings):
        print("Yes")
    else:
        print("No")
