#Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def cal(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return None

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    target = 7
    print(cal(arr, target))