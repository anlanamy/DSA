class BinaryTree:
    def __init__(self, rootObj, \
            left=None, right=None):             #可以同时设置节点的左右子树
        self.key = rootObj
        self.leftChild = left
        self.rightChild = right

    def insertLeft(self, newNode):
        self.leftChild = BinaryTree(newNode, \
                left=self.leftChild)

    def insertRight(self, newNode):
        self.rightChild = BinaryTree(newNode, \
                right = self.rightChild)

    def getRightChild(self):
        return self.rightChild;

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

def _print_t(tree, is_left, offset, depth, buf):
    if not tree:
        return 0

    b = '{:^5}'.format(tree.key)
    width = 5
    while len(buf)<2*depth+1:                #让后面的buf[2*depth]访问有效
        buf.append([])
    left  = _print_t(tree.leftChild,  True, offset,                depth + 1, buf);
    right = _print_t(tree.rightChild, False, offset + left + width, depth + 1, buf);

    enlarge = offset+left+width+right-len(buf[2*depth])
    buf[2*depth].extend([' ']*enlarge)
    for i, c in enumerate(b):               #输出子树根节点的内容
        buf[2*depth][offset+left+i] = c


    if depth > 0:                          #输出子树与其父节点的连线
        if is_left:
            enlarge = offset+left+2*width+right-len(buf[2*depth-1])
            buf[2*depth-1].extend([' ']*enlarge)
            for i in range(width+right):
                buf[2 * depth - 1][offset + left + width//2 + i] = '-'
            buf[2 * depth - 1][offset + left + width//2] = '+';
            buf[2 * depth - 1][offset + left + width//2 + right + width] = '+';
        else:
            enlarge = offset+left+width+right-len(buf[2*depth-1])
            buf[2*depth-1].extend([' ']*enlarge)
            for i in range(left+width):
                buf[2 * depth - 1][offset - width//2 + i] = '-';
            buf[2 * depth - 1][offset + left + width//2] = '+';
            buf[2 * depth - 1][offset - width//2 - 1] = '+';
    return left + width + right;

def print_t(tree):
    buf = []
    _print_t(tree, True, 0, 0, buf)
    for l in buf:
        print(''.join(l))

def tokenlize(expr):
    """
    支持的token类型
    运算符：‘+’，‘-’，‘*’，‘/’
    操作数：整数，标识符（以字母开头，包含字母或数字）
    括号：‘(’，‘)’
    """
    for _expr in expr.split():
        for i in _tokenlize(_expr):
            yield i
def _tokenlize(expr):                     #不用管表达式中的空格了
    buf = []
    for i in expr:
        if i in '+-*/()':
            if buf:
                yield ''.join(buf); buf=[]
            yield i
        elif i.isalnum():
            if buf and buf[0].isdigit() and i.isalpha():
                yield ''.join(buf); buf=[]
            buf.append(i)
        else:
            raise ValueError("Unknown charactor:'{}'".format(i))
    if buf:
        yield ''.join(buf); buf=[]
        
priority = {'(':0, '+':1, '-':1, '*':2, '/':2}
def buildParseTree(inexp):              #中缀表达式
    subtree_stack = []                  #用栈来保存中间过程中生成的子树
    op_stack = []                       #用栈来保存操作符。
    tokenlist=tokenlize(inexp)                                  #请参考以前表达式中缀转后缀的代码，
    for t in tokenlist:          #从字符串中提取token
        if t=='(':
            op_stack.append(t)
        elif t==')':
            while op_stack[-1]!='(':
                right=subtree_stack.pop()#从左向右书写表达式，所以先弹出的作为右节点
                left=subtree_stack.pop()
                currentTree=BinaryTree(op_stack.pop(),left,right)#栈内弹出建立子树
                subtree_stack.append(currentTree)
            op_stack.pop()
        elif t in '+-*/()':#操作数
            while op_stack!=[] and op_stack[-1]!= '(' and priority[op_stack[-1]] >= priority[t]:#先弹出比自己优先级高的子树
                right=subtree_stack.pop()
                left=subtree_stack.pop()
                currentTree=BinaryTree(op_stack.pop(),left,right)
                subtree_stack.append(currentTree)
            op_stack.append(t)
        else:  #字符与数字组合的处理
            currentTree=BinaryTree(t)
            subtree_stack.append(currentTree)
    
    while op_stack!=[]:#最后一步将表达式中所有的子树组合
        right=subtree_stack.pop()
        left=subtree_stack.pop()
        currentTree=BinaryTree(op_stack.pop(),left,right)
        subtree_stack.append(currentTree)
        
        # 这里原来有30行左右的代码，实现了从中缀表达式到二叉树结构的转换。
        # 现在它们被删掉了，请同学们重新实现。
        pass
    if len(subtree_stack) > 1:
        raise SyntaxError("Unexpected operand '{}'".format(subtree_stack[-1]))
    #最后子树栈中的唯一元素，就是我们要求的表达式树。
    return subtree_stack[0]

#下面的测试代码请不要改动，它从输入读取一行作为表达式字符串，然后完成两件事情：
#      1. 输出表达式中包括的单词
#      2. 调用buildParseTree进行二叉树转换，并把得到的表达式树打印出来。
#
if __name__ == "__main__":
    expr = input()
    #expr = "(a + b)*h/2"
    for t in tokenlize(expr):
        print(t)
    pt = buildParseTree(expr)
    print_t(pt)