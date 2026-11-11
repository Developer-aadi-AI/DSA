def unionArray(nums1, nums2):
    i = 0
    j = 0
    res = []

    while i < len(nums1) and j < len(nums2):

        if nums1[i] <= nums2[j]:
            if not res or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1

        else:
            if not res or res[-1] != nums2[j]:
                res.append(nums2[j])
            j += 1

    while i < len(nums1):
        if not res or res[-1] != nums1[i]:
            res.append(nums1[i])
        i += 1

    while j < len(nums2):
        if not res or res[-1] != nums2[j]:
            res.append(nums2[j])
        j += 1

    return res

print(unionArray([1,1,1,2,2,3,4,], [1,1,2,2,2,3,4]))