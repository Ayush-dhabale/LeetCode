'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
'''
'''
class MedianFinder:


'''
from heapq import heappop,heappush
class MedianFinder:
    '''
    #Brute
    def __init__(self):
        self.nums = []
        self.n = 0
        

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.n += 1
        

    def findMedian(self) -> float:
        self.nums.sort()
        if self.n % 2 == 0:
            return (self.nums[self.n // 2] + self.nums[self.n // 2 - 1]) / 2.0

        return self.nums[self.n // 2]
    '''
    #Optimal
    def __init__(self):
        self.minheap = []
        self.min = 0
        self.maxheap = []
        self.max = 0

    def addNum(self, num: int) -> None:
        if self.max == 0 or self.maxheap[0] >= num:
            heappush(self.maxheap,-num)
            self.max += 1
        else:
            heappush(self.minheap,num)
            self.min += 1
            
        if self.max > self.min + 1:
            heappush(self.minheap,- heappop(self.maxheap))
            self.min += 1
            self.max -= 1
            
        elif self.max < self.min:
            heappush(self.maxheap,- heappop(self.minheap))
            self.max += 1
            self.min -= 1
        

    def findMedian(self) -> float:
        if self.max == self.min:
            return self.minheap[0] / 2.0 - self.maxheap[0] / 2.0
        
        return - self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()