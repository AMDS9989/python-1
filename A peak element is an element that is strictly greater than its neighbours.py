def find_peak_element(nums):
    left, right = 0, len(nums) - 1   
    while left < right:
        mid = left + (right - left) // 2        
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid    
    return left
nums = [1, 2, 3, 1]
shahid bhai

