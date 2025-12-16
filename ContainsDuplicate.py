def ContainsDuplicate(nums):
    a = set(nums)
    if len(a) != len(nums):
        return True 
    return False 
abc = [ 1,2,3,4,5,6,7,7]
print(ContainsDuplicate(abc))