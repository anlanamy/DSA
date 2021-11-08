def bsearch(nums: [int], target: int) -> int:
    if len(nums)==0:
        return -1
    else:
        first=0
        last=len(nums)-1
        found=False
        if target>nums[-1]:#先判断两个临界情况
            return -2-last
        if target<nums[0]:
            return -1
        while first<last-1 and not found:
            midpoint=(first+last)//2
            if nums[midpoint]==target:
                found=True
                return midpoint
            else:
                if target<nums[midpoint]:
                    last=midpoint#由于target不一定在列表中，所以需要从midpoint开始寻找
                else:
                    first=midpoint
        if not found:
            if nums[first]==target:
                return first
            elif nums[last]==target:
                return last
            else:
                return -2-first

if __name__ == '__main__':
    nums = [int(s) for s in input().split()]
    target = int(input())
    # nums = [1, 3, 5, 6]
    # target = 2
    print(bsearch(nums, target))
