def qsort(nums: [int]) -> [int]:
    if len(nums)==0 or len(nums)==1:
        return nums
    else:
        qsortHelper(nums,0,len(nums)-1)
    return nums

def qsortHelper(nums,first,last):
    if first<last:
        splitpoint=partition(nums,first,last)
        qsortHelper(nums,first,splitpoint-1)
        qsortHelper(nums,splitpoint+1,last)
        
def partition(nums,first,last):
    median=(first+last+1)//2
    if nums[median]<nums[first]:
        #采取第一个元素、中间元素、最后一个元素作为取中位数的三点，
        #这样取样可以保证比只使用第一个元素更靠近中位数，且可以避免有序数组排序的时间复杂性，理论上分拆后算法效率会提高
        temp=nums[median]        
        nums[median]=nums[first]
        nums[first]=temp
    if nums[first]>nums[last]:
        temp=nums[last]        
        nums[last]=nums[first]
        nums[first]=temp
    if nums[median]>nums[last]:
        temp=nums[last]        
        nums[last]=nums[first+1]
        nums[first+1]=temp
        
    temp=nums[first+1]
    nums[first+1]=nums[median]
    nums[median]=temp
    
    pivotvalue=nums[first+1]
    leftmark=first+2
    rightmark=last
    done=False
    while not done:
        while leftmark<=rightmark and nums[leftmark]<=pivotvalue:
            leftmark+=1
        while rightmark>=leftmark and nums[rightmark]>=pivotvalue:
            rightmark-=1
        if rightmark<leftmark:
            done=True
        else:
            temp=nums[leftmark]
            nums[leftmark]=nums[rightmark]
            nums[rightmark]=temp
    
    nums[first+1]=nums[rightmark]
    nums[rightmark]=pivotvalue
        
    return rightmark
    
if __name__ == '__main__':
    numbers = [int(s) for s in input().split()]
    # numbers = [5, 1, 1, 2, 0, 0]
    sorted_numbers = qsort(numbers)
    print(' '.join([str(i) for i in sorted_numbers]))

