import heapq
laptops = [
    {'name': 'ThinkPad', 'amount': 100, 'price': 91.1},
    {'name': 'Mac', 'amount': 50, 'price': 543.22},
    {'name': 'Surface', 'amount': 200, 'price': 21.09},
    {'name': 'Alienware', 'amount': 35, 'price': 31.75},
    {'name': 'Lenovo', 'amount': 45, 'price': 16.35},
    {'name': 'Huawei', 'amount': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, laptops, key=lambda s: s['price'])
expensive = heapq.nlargest(3, laptops, key=lambda s: s['price'])

import heapq

class PriorityQueue:
  
  def __init__(self):
    self._queue = []
    self._index =0
    
  def push(self, item, priority):
    # 传入两个参数，一个是存放元素的数组，另一个是要存储的元素，这里是一个元组。
    # 由于heap内部默认有小到大排，所以对priority取负数
    heapq.heappush(self._queue, (-priority, self._index, item))
    self._index += 1
  
  def pop(self):
    return heapq.heappop(self._queue)[-1]