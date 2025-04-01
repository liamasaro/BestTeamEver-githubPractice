def remove_duplicates(arr): # function to remove duplicates in an array
    arr.sort() # sorts the array
    unique_arr = [] # creates a new unique array
    removed_elements = [] # creates an empty array to store the removed elements
    for i in range(len(arr)): # for loop to iterate through passed in array, arr 
        if i == 0 or arr[i] != arr[i-1]: # if @ the first array element OR an array element is not duplicate of the one prior to it 
            unique_arr.append(arr[i]) # append the element to the unique array 
        else: # otherwise
            removed_elements.append(arr[i]) # if the element is a duplicate, append to removed elements array
    return unique_arr, removed_elements # return both arrays

# Test the function
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr, removed_elements = remove_duplicates(arr)
print("Original array:", arr)
print("Unique array:", unique_arr)
print("Removed elements:", removed_elements)
