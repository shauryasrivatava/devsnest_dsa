class KthLargest(object):
    def __init__(self, k, nums):
        import heapq
        self.array = list()
        self.k = k
        for num in nums:
            heapq.heappush(self.array, num)
            if len(self.array) > self.k:
                heapq.heappop(self.array)
                
    def add(self, val):
        heapq.heappush(self.array, val)
        if len(self.array) > self.k:
            heapq.heappop(self.array)
        
        return self.array[0]
        
