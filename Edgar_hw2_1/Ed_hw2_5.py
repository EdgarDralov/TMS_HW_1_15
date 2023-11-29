# Create list

list_a = [10, 15, 1, 15, 10, 1, 6, 6, 15, 11, -4, -10, -10]

# Convert list to a SET to remove duplicates
unique_value_set = set(list_a)

# Convert the set back
result_list=list(unique_value_set)

# Print
print("list without duplicate:", result_list)
