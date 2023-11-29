# Create numbers_list
numbers_list = [10, 20, 30, 40, 50, 20, 60]
# Boolean flag to check if 20 found
found_20 = False

# Change 20 to 200
for index, num in enumerate(numbers_list):
    if num == 20 and not found_20:
        numbers_list[index] = 200
        found_20 =True
        break
print("Updated list:", numbers_list)

# ------------------------------------------------------------------------------------------------

# Code if we want update all 20 in list

numbers_list2 = [10, 20, 30, 40, 50, 20, 60]
for index, num in enumerate(numbers_list):
    if num == 20:
        numbers_list2[index] = 200
print("updated_list", numbers_list2)