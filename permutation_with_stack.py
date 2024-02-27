def to_permutation(arr):
    stack = []
    count = 0
    
    for num in arr:
        if num not in stack:
            stack.append(num)
        else:
            # If the number is already in the stack, find the next available unique number
            index = stack.index(num)
            unique_num = num + 1
            while unique_num in stack:
                unique_num += 1
            stack.insert(index, unique_num)
            count += 1
    # Ensure the length of the stack is the same as the length of the input list
    while len(stack) < len(arr):
        # Find the next available unique number
        unique_num = max(stack) + 1
        while unique_num in stack:
            unique_num += 1
        stack.append(unique_num)
        count += 1
  

    return count, stack


# Test case
numbers = [3,3, 5, 5, 6, 6,7,7,9]
new_list = to_permutation(numbers)
print("Modified list:", new_list)