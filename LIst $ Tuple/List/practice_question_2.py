list = [1, 2, 3, 2, 1]  # Given list

copy_list = list.copy()  # Create a copy of the list

list.reverse()  # Reverse the original list

# Check if the reversed list is equal to the copy
if copy_list == list:
    print("Palindrom")  # It's a palindrome!
else:
    print("NOT palindrom")  # It's not a palindrome.
