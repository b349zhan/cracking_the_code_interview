from q11 import assertions

def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi + 1, r, nums)

def isUnique_withoutDataStructure(s):
    # Using sorting algorithm and check each neighbor
    # Due to python immutable strings, have to check with extra list
    if len(s) < 2: return True
    list_s = list(s)
    quicksort(0, len(s)-1, list_s)
    for i in range(len(s)-1):
        if list_s[i] == list_s[i+1]: return False
    return True

if __name__ == "__main__":
    assertions(isUnique_withoutDataStructure)
    