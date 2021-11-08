#uuid_share#  4d8c88f1-3904-4a93-a2fd-d545ce276f83  #
class Stack(list):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]

    def isEmpty(self):
        return self == []

    def size(self):
        return len(self)

    def __repr__(self):
        l = len(self) * 7
        s = "|" + "-" * l + ")\n|"
        for a in self:
            s += "| %-5s" % a
        s += "\n|" + "-" * l + ")"
        return s
    __str__ = __repr__

def houzhuiqiuzhi(str):
    s=Stack()
    tokenlist=str.split()
    for t in tokenlist:
        if t in "0123456789":
            s.push(int(t))
            print(s)
        else:
            cal2=s.pop()
            print(s)
            cal1=s.pop()
            print(s)
            result=calculate(t,cal1,cal2)
            s.push(result)
            print(s)
    return s.pop()

def calculate(symb,num1,num2):
    if symb=="*":
        return num1*num2
    if symb=="+":
        return num1+num2
    if symb=="-":
        return num1-num2
    if symb=="/":
        return num1/num2

for str in ["2 3 * 4 +","1 2 + 3 + 4 + 5 +","1 2 3 4 5 * + * +"]:
    print(str)
    print(houzhuiqiuzhi(str))