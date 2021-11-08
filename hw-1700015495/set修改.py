class Set:
    def __init__(self):
        # 为方便测试，请将初始table大小设为11。变量可随意添加或修改
        self.table_size = 11
        self.slots = [None] * self.table_size
        self.length=0

    def add(self, key: int) -> None:
        hashvalue=key%self.table_size
        nextslot=hashvalue
        written=False
        while self.slots[nextslot]!=None:#如果冲突就+1线性寻找，由于之前可能存在冲突过的元素被删除，所以结束条件是找到None才能保证没有重复元素
            if self.slots[nextslot]=='' and not written:#之前删除过的空槽插入，注意要之前没有填入过
                self.slots[nextslot]=key
                written=True#标记已经填入过元素
            elif self.slots[nextslot]==key:#如果找到key则将其删除，保持set的元素唯一性
                self.length-=1
                if not written:
                    self.slots[nextslot]=''
                else:
                    written=True
                break
            nextslot=(nextslot+1)%self.table_size
        if not written:
            self.slots[nextslot]=key
        self.length+=1
        if len(self)>=0.5*self.table_size:#负载因子大于0.5时扩列,否则速度会很慢
            self.resize()
        pass
    
    def resize(self):
        oldtable=self.slots
        self.table_size=self.table_size*5#将列表扩充成为原来的五倍
        self.slots=[None] * self.table_size
        self.length=0
        for slot in oldtable:#对于旧列表中的元素一一进行添加
            if slot!=None and slot!='':
                self.add(slot)

    def __contains__(self, key: int) -> bool:
        found=False
        hashvalue=key%self.table_size
        while self.slots[hashvalue]!=None and not found:
            if self.slots[hashvalue]==key:
                found=True
            else:
                hashvalue=(hashvalue+1)%self.table_size#继续向下线性寻找，直到搜寻到空元素
        return found

    def __len__(self) -> int:
        return self.length

    def remove(self, key: int) -> None:
        hashvalue=key%self.table_size
        while self.slots[hashvalue]!=None:
            if self.slots[hashvalue]==key:
                self.slots[hashvalue]=''
                self.length-=1
                break
            else:
                hashvalue=(hashvalue+1)%self.table_size#继续向下线性寻找，直到搜寻到空元素
        pass     


if __name__ == '__main__':
    in_arr = input().split()
    # in_arr = "add 1 add 2 add 1 len contains 1 contains 3".split()
    s = Set()
    out_arr = []
    i = 0
    while i < len(in_arr):
        if in_arr[i] == 'add':
            s.add(int(in_arr[i + 1]))
            i += 2
        elif in_arr[i] == 'contains':
            re = int(in_arr[i + 1]) in s
            out_arr.append(str(re))
            i += 2
        elif in_arr[i] == 'len':
            length = len(s)
            out_arr.append(str(length))
            i += 1
        elif in_arr[i] == 'remove':
            s.remove(int(in_arr[i + 1]))
            i += 2
    print(' '.join(out_arr))
