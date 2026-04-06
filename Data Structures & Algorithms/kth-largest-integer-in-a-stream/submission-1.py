class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        

    def add(self, val: int) -> int:
        self.nums.append(val)
        nums1 = sorted(self.nums)
        return nums1[len(nums1) - self.k]

        
