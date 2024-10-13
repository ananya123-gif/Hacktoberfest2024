def findMedianSortedArrays(nums1, nums2):
    l=[]
    for i in range(len(nums1)):
        l.append(nums1[i])
    for j in range(len(nums2)):
        l.append(nums2[j])
    l.sort()
    n=len(l)
    if(n%2==0):
        return (l[(n//2)-1]+l[(n//2)])/2
    else:
        return (l[n//2])


# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
