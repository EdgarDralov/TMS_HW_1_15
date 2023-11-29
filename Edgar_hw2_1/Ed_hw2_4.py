# Input the values n and x
n = int(input("Enter n: "))
x = input("Enter x: ")

# Create list
result_list = [x] * n

# Convert list to str
result_list = ', '.join(result_list)
# Display
print("[" + result_list + "]")