# Get user input for the list of numbers
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Get the target value from the user
target = int(input("Enter the target value: "))

a = []

# Find the indices where the sum of two numbers equals the target
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):  # Avoid repeating pairs by starting j from i+1
        if nums[i] + nums[j] == target:
            a.append(i)
            a.append(j)
            break  # Once we find a valid pair, no need to continue

# Print the result
print(f"Indices of the numbers that add up to the target: {a}")
