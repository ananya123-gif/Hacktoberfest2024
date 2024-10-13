def trap(self, height: List[int]) -> int:
    l=len(height)
    big_left=[height[0]]*l
    big_right=[height[-1]]*l

    for i in range(l):
        big_left[i]=max(big_left[i-1],height[i])
        big_right[-i-1]=max(big_right[-i],height[-i-1])

    return sum(min(big_left[i],big_right[i])-height[i] for i in range(l))


# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
