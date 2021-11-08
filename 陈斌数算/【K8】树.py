#一、
#写一个buildTree函数（返回一个BinaryTree对象）, 函数通过调用BinaryTree类方法，返回如图所示的二叉树：
class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return  self.rightChild

    def setRootVal(self,obj):
        self.key=obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        def LBFS(tree):
            LieBiaoFangShi='['
            if tree:
                LieBiaoFangShi += str(tree.getRootVal())
                LieBiaoFangShi += ',' + LBFS(tree.getLeftChild())
                LieBiaoFangShi += ',' + LBFS(tree.getRightChild())
            LieBiaoFangShi += ']'
            return LieBiaoFangShi
        return LBFS(self)

    def height(self):
        def H(tree):
            if tree:
                h = 1 + max(H(tree.getLeftChild()),H(tree.getRightChild()))
            else:
                h = 0
            return h
        return H(self)


def buildTree():
    r=BinaryTree('a')
    r.insertLeft('b')
    r.getLeftChild().insertRight('d')
    r.insertRight('c')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    return r

#二、
# 为链接实现的BinaryTree类写一个__str__方法，把二叉树的内容用嵌套列表的方式打印输出。
#编写程序：
#扩展了的BinaryTree类定义，以及buildTree函数的Python代码
print(buildTree())

#三、
# 请为链接实现的BinaryTree类写一个height方法，返回树的高度。
#编写程序：
#BinaryTree类的height方法；
print(buildTree().height())#（能够返回3）