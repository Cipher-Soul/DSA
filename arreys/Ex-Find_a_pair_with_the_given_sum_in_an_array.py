# Find a pair with the given sum in an array
'''
    Given an unsorted integer array, find a pair with the given sum in it.
    example: nums = [8,7,2,5,3,1]
    target =10
     output:
     Pair found (8, 2)
     or
     Pair found (7, 3)
      
    Input:   nums = [5, 2, 6, 8, 1, 9] target = 12  Output: Pair not found 
'''
#Method 1 - brute force method ||  --time complexity of the above solution is O(n2)
def find_pair_of(nums,target):
    pair_result = []
    if len(nums) ==1 and nums[0]==target:
        return nums
    for x in nums:
        for y in nums:
            if x + y == target:
                pair_result.append([x,y])
            
    return pair_result

if __name__ == '__main__':  
    test_case = [
        [
            [2, 7, 11, 15],9    
        ],
        [
            [-10, 20, 10, -20],0
        ],
        [
            [1, 5, 3, 7, 5, 2],10
        ],
        [
            [0, 4, 3, 0],0
        ],
        [
            [1, 2, 3, 4],10
        ],
        [
            [],5
        ],
        [
            [5],5
        ],
        [
             [1, 5, 5, 3],10
        ]
    ]  
    for case in test_case:
        
        nums = case[0]
        target= case[1]
        result = find_pair_of(nums,target)
        print(result)