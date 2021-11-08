class Map:
    def __init__(self):
        # 为方便测试，请将table大小设为100003。变量可随意添加或修改
        self.table_size = 100003
        self.slots = [[] for _ in range(self.table_size)]#在初始我们就将每一个节点设置成为一个列表，方便后续的添加
        self.data = [[] for _ in range(self.table_size)]
        self.length=0

    def put(self, key: int, value: int) -> None:
        hashvalue=key%self.table_size
        found=False
        for i in range(len(self.slots[hashvalue])):
            if self.slots[hashvalue][i]==key:
                self.data[hashvalue][i]=value
                found=True
                break
        if not found:
            self.slots[hashvalue].append(key)#向数据链中添加
            self.data[hashvalue].append(value) 
            self.length+=1
        pass

    def get(self, key: int) -> int:
        hashvalue=key%self.table_size
        found=False
        for i in range(len(self.slots[hashvalue])):
            if self.slots[hashvalue][i]==key:
                return self.data[hashvalue][i]
                found=True
                break
        if not found:
            return None

    def remove(self, key: int) -> None:
        hashvalue=key%self.table_size
        for i in range(len(self.slots[hashvalue])):
            if self.slots[hashvalue][i]==key:
                del self.data[hashvalue][i]
                del self.slots[hashvalue][i]
                self.length-=1
                break
        pass

    def __setitem__(self, key: int, value: int) -> None:
        hashvalue=key%self.table_size
        found=False
        for i in range(len(self.slots[hashvalue])):
            if self.slots[hashvalue][i]==key:
                self.data[hashvalue][i]=value
                found=True
                break
        if not found:
            self.slots[hashvalue].append(key)#向数据链中添加
            self.data[hashvalue].append(value) 
            self.length+=1
        pass

    def __getitem__(self, key: int) -> int:
        hashvalue=key%self.table_size
        found=False
        for i in range(len(self.slots[hashvalue])):
            if self.slots[hashvalue][i]==key:
                return self.data[hashvalue][i]
                found=True
                break
        if not found:
            return None

    def __delitem__(self, key: int) -> None:
        hashvalue=key%self.table_size
        for i in range(len(self.slots[hashvalue])):
            if self.slots[hashvalue][i]==key:
                del self.data[hashvalue][i]
                del self.slots[hashvalue][i]
                self.length-=1
                break
        pass

    def __len__(self) -> int:
        return self.length

    def __contains__(self, key: int) -> bool:
        hashvalue=key%self.table_size
        return key in self.slots[hashvalue]


if __name__ == '__main__':
    in_arr = input().split()
    # in_arr = "put 1 2 put 1 3 get 1 len contains 1 remove 1 len".split()
    m = Map()
    out_arr = []
    i = 0
    while i < len(in_arr):
        if in_arr[i] == 'put':
            m.put(int(in_arr[i + 1]), int(in_arr[i + 2]))
            i += 3
        elif in_arr[i] == 'get':
            value = m.get(int(in_arr[i + 1]))
            out_arr.append(str(value))
            i += 2
        elif in_arr[i] == 'remove':
            m.remove(int(in_arr[i + 1]))
            i += 2
        elif in_arr[i] == 'len':
            length = len(m)
            out_arr.append(str(length))
            i += 1
        elif in_arr[i] == 'contains':
            re = int(in_arr[i + 1]) in m
            out_arr.append(str(re))
            i += 2
    print(' '.join(out_arr))
