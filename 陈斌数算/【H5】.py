# uuid#  eff6a8fb-6f5a-4c66-808f-74655dc512ce  #
# SESSDSA20课程上机作业
# 【H5】AVL树作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中指定部位编写代码
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业代码部分在4月29日18:00之前提交到PyLn编程学习系统，班级码见Canvas系统

# ---- 用AVL树实现字典类型 ----
# 用AVL树来实现字典类型，使得其put/get/in/del操作均达到对数性能
# 采用如下的类定义，至少实现下列的方法
# key至少支持整数、浮点数、字符串
# 请调用hash(key)来作为AVL树的节点key
# 【注意】涉及到输出的__str__, keys, values这些方法的输出次序是AVL树中序遍历次序
#    也就是按照hash(key)来排序的，这个跟Python 3.7中的dict输出次序不一样。

# 请在此编写你的代码


class TreeNode:
    """
    二叉树节点
    请自行完成节点内部的实现，并实现给出的接口
    """

    def __init__(self, key, val, left=None, right=None, parent=None):  # 初始化方法
        self.key = hash(key)
        self.ori_key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

    def getLeft(self):  # 获取左子树 (不存在时返回None)
        return self.leftChild

    def getRight(self):  # 获取右子树 (不存在时返回None)
        return self.rightChild

    hasLeftChild = getLeft
    hasRightChild = getRight

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = hash(key)
        self.ori_key = key
        self.payload = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def replaceNodeValue(self, key, val):
        self.key = hash(key)
        self.ori_key = key
        self.payload = val

    def __str__(self):
        lcstr = f"[{str(self.leftChild)}]" if self.leftChild else "[]"
        rcstr = f"[{str(self.rightChild)}]" if self.rightChild else "[]"
        return f"[{repr(self.ori_key)},{lcstr},{rcstr}]"

    __repr__ = __str__

    def __iter__(self):
        if self.hasLeftChild():
            for ori_key in self.leftChild:
                yield ori_key
        yield self.ori_key
        if self.hasRightChild():
            for ori_key in self.rightChild:
                yield ori_key

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


class mydict:
    """
    以AVL树作为内部实现的字典
    """

    def getRoot(self):  # 返回内部的AVL树根
        return self.avlTree.root

    def __init__(self):  # 创建一个空字典
        self.avlTree = AVLTree()

    def __setitem__(self, key, value):  # 将key:value保存到字典
        # md[key]=value
        self.avlTree[key] = value

    def __getitem__(self, key):  # 从字典中根据key获取value
        # v = md[key]
        # key在字典中不存在的话，请raise KeyError
        return self.avlTree[key]

    def __delitem__(self, key):  # 删除字典中的key
        # del md[key]
        # key在字典中不存在的话，请raise KeyError
        del self.avlTree[key]

    def __len__(self):  # 获取字典的长度
        # l = len(md)
        return len(self.avlTree)

    def __contains__(self, key):  # 判断字典中是否存在key
        # k in md
        return key in self.avlTree

    def clear(self):  # 清除字典
        self.avlTree = AVLTree()

    def __str__(self):  # 输出字符串形式，参照内置dict类型，输出按照AVL树中序遍历次序
        # 格式类似：{'name': 'sessdsa', 'hello': 'world'}
        return str(self.avlTree)

    __repr__ = __str__

    def keys(self):  # 返回所有的key，类型是列表，按照AVL树中序遍历次序
        retlist = []
        for k in self.avlTree:
            retlist.append(k)
        return retlist

    def values(self):  # 返回所有的value，类型是列表，按照AVL树中序遍历次序
        retlist = []
        for k in self.avlTree:
            retlist.append(self.avlTree[k])
        return retlist


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        if self.root:
            return iter(self.root)
        return iter([])

    def __str__(self):
        allstr = ", ".join([f"{repr(key)}: {repr(self[key])}" for key in self])
        return f"{{{allstr}}}"

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            self.size = 1

    __setitem__ = put

    def _put(self, key, val, currentNode):
        ori_key = key
        key = hash(ori_key)
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(ori_key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(ori_key, val, parent=currentNode)
                self.size += 1
                self.updateBalance(currentNode.leftChild)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(ori_key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(ori_key, val, parent=currentNode)
                self.size += 1
                self.updateBalance(currentNode.rightChild)
        else:
            currentNode.replaceNodeValue(ori_key, val)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.hasLeftChild():
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 \
                                - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 \
                                + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.hasRightChild():
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot

        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 \
                                - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 \
                                + min(rotRoot.balanceFactor, 0)

    def get(self, key):
        return self._get(key, self.root).payload

    __getitem__ = get

    def _get(self, key, currentNode):
        ori_key = key
        key = hash(ori_key)
        if not currentNode:
            raise KeyError(ori_key)
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(ori_key, currentNode.leftChild)
        else:
            return self._get(ori_key, currentNode.rightChild)

    def __contains__(self, key):
        try:
            v = self[key]
        except KeyError:
            return False
        return True

    def delete(self, key):
        ori_key = key
        key = hash(ori_key)
        if self.size > 1:
            nodeToRemove = self._get(ori_key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError(ori_key)
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError(ori_key)

    __delitem__ = delete

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
                currentNode.parent.balanceFactor -= 1
            else:
                currentNode.parent.rightChild = None
                currentNode.parent.balanceFactor += 1
            self.updateBalanceRemove(currentNode.parent)
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            if succ.isLeftChild():
                succ.parent.balanceFactor -= 1
            else:
                succ.parent.balanceFactor += 1
            succ.spliceOut()
            currentNode.replaceNodeValue(succ.ori_key, succ.payload)
            self.updateBalanceRemove(succ.parent)
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                    currentNode.parent.balanceFactor -= 1
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                    currentNode.parent.balanceFactor += 1
                else:  # 自己是根
                    currentNode.leftChild.parent = None
                    self.root = currentNode.leftChild
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                    currentNode.parent.balanceFactor -= 1
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                    currentNode.parent.balanceFactor += 1
                else:
                    currentNode.rightChild.parent = None
                    self.root = currentNode.rightChild
            if currentNode.parent:
                self.updateBalanceRemove(currentNode.parent)

    def updateBalanceRemove(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            node = node.parent
        if node.balanceFactor == 0 and node.parent:
            if node.isLeftChild():
                node.parent.balanceFactor -= 1
            elif node.isRightChild():
                node.parent.balanceFactor += 1
            self.updateBalanceRemove(node.parent)


# 代码结束


# mydict=dict
# 检验
print("========= AVL树实现字典 =========")
md = mydict()
md['7'] = '5'
md['0'] = '0'
md['1'] = '4'
md['5'] = '1'
md['1'] = '4'
print("1" in md)

,__setitem__('3','8'),__contains__('4'),__setitem__('5','1'),__len__(),__setitem__('8','0'),__setitem__('1','2'),values(),try __getitem__(1.0),try __delitem__(1.0),try __getitem__(3.0),try __delitem__(3.0),try __getitem__(5.0),try __delitem__(5.0),try __getitem__(5),try __delitem__(5),try __getitem__('4'),try __delitem__('4')
values()
__setitem__('2','2')
__contains__('1')
__setitem__('9','9')
values()
__setitem__('6','2')
values()
clear()
values()
__setitem__('7','3')
__setitem__('7','8')
__contains__('3')
__setitem__('0','4')
__len__()
__contains__('1')
__setitem__('0','0')
__len__()
__setitem__('1','4')
__getitem__('0')
__setitem__('7','5')
__delitem__('1')
__contains__('2')
__setitem__('3','8')
__contains__('4')
__setitem__('5','1')
__len__()
__setitem__('8','0')
__setitem__('1','2')
values()
