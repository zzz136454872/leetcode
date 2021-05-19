
def kLargestSub(nums,l,r,k):
    l0=l
    r0=r
    test=nums[l]
    while l<r:
        while l<r and nums[r]>test:
            r-=1
        nums[l]=nums[r]
        while l<r and nums[l]<=test:
            l+=1
        nums[r]=nums[l]
    nums[l]=test
    # print(nums,test,l,r,k)
    if l==k:
        return nums[l]
    if l>k:
        return kLargestSub(nums,l0,l-1,k)
    else:
        return kLargestSub(nums,l+1,r0,k)

def kLargest(nums,k):
    """返回nums中第k大的数，从1开始计数
    领会精神就可以，其实比sorted后取值还慢
    """
    if k<1 or k>len(nums):
        return -12345
    return kLargestSub(nums,0,len(nums)-1,len(nums)-k)
