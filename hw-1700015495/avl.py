def _print_t(tree, is_left, offset, depth, buf, label):
    if not tree:
        return 0

    b = "{:^5}".format(label(tree))
    width = 5
    while len(buf)<2*depth+1:                #让后面的buf[2*depth]访问有效
        buf.append([])
    left  = _print_t(tree.leftChild,  True, offset,                depth + 1, buf, label);
    right = _print_t(tree.rightChild, False, offset + left + width, depth + 1, buf, label);

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

def print_t(tree, label=lambda x:x.key):
    buf = []
    _print_t(tree, True, 0, 0, buf, label)
    for l in buf:
        print(''.join(l))

class TreeNode:
    def __init__(self, key, val, left=None,
                right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent             #增加了对parent的指回
        self.balanceFactor = 0           #在BST中用不到，也没什么坏处。
        self.height=0

    def hasLeftChild(self):              #这个函数实际没必要，只是为了代码的讲解更加口语化。
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def isLeaf(self):
        return not self.hasAnyChildren()

    def flat(self):
        flat = lambda x: flat(x.leftChild)+[x.key]+flat(x.rightChild) if x else []
        return flat(self)

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():           #让左右子节点指回父节点
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        if self.hasRightChild():         #在BinarySearchTree.remove()中的唯一可能
            return self.rightChild.findMin()
        elif self.isRoot():
            return None
        elif self.isLeftChild():
            return self.parent
        else : #self.isRightChild()       #在parent子树中的最末
            self.parent.rightChild = None #暂时移除自己
            succ = self.parent.findSuccessor()
            self.parent.rightChild = self #恢复自己
            return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():     #往左下角
            current = current.leftChild
        return current

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

class BinarySearchTree:              #函数太多了，增加了“树”类来管理与之有关的部分
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return self.size
    def __len__(self):               #供len(bst)调用
        return self.size
    def __iter__(self):
        return self.root.__iter__()

    def display(self):
        print_t(self.root)

    def put(self,key,val=0):
        if self.root:
            self.size += self._put(key,val,self.root)
        else:
            self.root = TreeNode(key, val)
            self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:            #递归左子树
            if currentNode.hasLeftChild():
                return self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = \
                    TreeNode(key, val, parent=currentNode)
                return 1
        elif key > currentNode.key:          #递归右子树
            if currentNode.hasRightChild():
                return self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = \
                    TreeNode(key, val, parent=currentNode)
                return 1
        else: #key == currentNode.key        #出现重复key
            currentNode.payload = val
            return 0

    def __setitem__(self, k, v):
        self.put(k,v)

    def get(self, key):
        if self.root:            #这里的判断和_get()内部的判断重复了
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else: #currentNode.key < key
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None           #删除根节点
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():              #作为叶节点的最简单情况
            #移除叶节点只需要在它的父节点中把它移除
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            elif currentNode.isRightChild():
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():    #有左右两个子节点的复杂情况
            succ = currentNode.findSuccessor() #前驱、后继肯定都有
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            self.remove(succ)                  #succ没有左子节点，为什么？不会出现第二层递归
        else:                                  #只有一个子节点的情况
            # 取得唯一子节点，不关心左右
            child = currentNode.leftChild \
                    if currentNode.hasLeftChild() \
                    else currentNode.rightChild  #可以砍掉一半的源代码
            if currentNode.isLeftChild():     #用子节点替换当前节点
                currentNode.parent.leftChild = child
                child.parent = currentNode.parent
            elif currentNode.isRightChild():
                currentNode.parent.rightChild = child
                child.parent = currentNode.parent
            else :                            #当前节点是根节点，直接替换成子节点
                currentNode.replaceNodeData(child.key,
                                           child.payload,
                                           child.leftChild,
                                           child.rightChild)

class AVL(BinarySearchTree):
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                return self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)  #调整平衡因子
                return 1
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                return self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)  #调整平衡因子
                return 1
        else: #key == currentNode.key
            currentNode.payload = val         #无新增节点，平衡因子不变
            return 0

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1: #先看自己是否要调整
            self.rebalance(node)                       #重新平衡，并且不会向上传递
            return
        if node.parent != None:                            #更新父节点平衡因子
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:             #调整父节点平衡因子
                self.updateBalance(node.parent)            #"=0"也会阻断递归的传递

    def DeleteUpdateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1: #先看自己是否要调整
            self.rebalance(node)
                       
        elif node.parent != None:  #如果自己不调整节点，直接对父节点进行调整
            if node.isLeftChild():
                node.parent.balanceFactor -= 1
            elif node.isRightChild():
                node.parent.balanceFactor += 1
                
        if node.parent!=None and (node.parent.balanceFactor > 1 or node.parent.balanceFactor < -1): #父节点是否要调整
                self.rebalance(node.parent)        
        if node.parent!=None and node.parent.balanceFactor == 0:  #当父节点的平衡因子恰好调整为0时需要继续向上调整
                self.DeleteUpdateBalance(node.parent)
                """if node.parent.balanceFactor > 1 or node.parent.balanceFactor < -1: #父节点是否要调整
                self.rebalance(node.parent)                       #重新平衡
            if node.parent.balanceFactor == 0: #当父节点的平衡因子恰好调整为0时需要继续向上调整
                self.DeleteUpdateBalance(node.parent)"""

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild                      #把新根节点提上来
        rotRoot.rightChild = newRoot.leftChild            #给新根节点的左子节点重新找位置
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot            #   并给它指定新的parent
        newRoot.parent = rotRoot.parent                   #新根节点完全取代旧根节点
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        #调整新、旧根节点的平衡因子，为什么这样？马上推导。
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
                                1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
                                1 + max(rotRoot.balanceFactor, 0)
        #self.display()

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild    #56，58新根的右子转为旧根的左子
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent           #59，64/66新根取代旧根和父建立关系
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot              #67，68旧根下沉为新根的子节点
        rotRoot.parent = newRoot
        #调整新、旧根节点的平衡因子，为什么这样？马上推导。
        rotRoot.balanceFactor = rotRoot.balanceFactor - \
                                1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - \
                                1 + min(rotRoot.balanceFactor, 0)
        #self.display()

    def rebalance(self, node):   #"<-1"或">1"才会被updateBalance调用
        if node.balanceFactor < -1:  #右重需要左旋
            if node.rightChild.balanceFactor > 0:
                # 右子节点左重，先对它进行一次右旋
                self.rotateRight(node.rightChild)
                #self.display()
            #正常左旋
            self.rotateLeft(node)
        elif node.balanceFactor > 1:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                #self.display()
            self.rotateRight(node)

    def get(self, key):
        if self.root:            #这里的判断和_get()内部的判断重复了
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else: #currentNode.key < key
            return self._get(key, currentNode.rightChild)

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None           #删除根节点
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')
            
    def remove(self,currentNode):
        if currentNode.isLeaf():              #作为叶节点的最简单情况
            #移除叶节点只需要在它的父节点中把它移除
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
                currentNode.parent.balanceFactor-=1
            elif currentNode.isRightChild():
                currentNode.parent.rightChild = None
                currentNode.parent.balanceFactor+=1
            self.DeleteUpdateBalance(currentNode.parent)
            
        elif currentNode.hasBothChildren():    #有左右两个子节点的复杂情况
            succ = currentNode.findSuccessor() #前驱、后继肯定都有
            #succFather=succ.parent
            #self.DeleteUpdateBalance(succFather)
            currentNode.key = succ.key
            currentNode.payload = succ.payload
            self.remove(succ)
            
        else:                                  #只有一个子节点的情况
            # 取得唯一子节点，不关心左右
            child = currentNode.leftChild \
                    if currentNode.hasLeftChild() \
                    else currentNode.rightChild  #可以砍掉一半的源代码
            if currentNode.isLeftChild():     #用子节点替换当前节点
                currentNode.parent.leftChild = child
                child.parent = currentNode.parent
                child.parent.balanceFactor-=1
                self.DeleteUpdateBalance(currentNode.parent)
            elif currentNode.isRightChild():
                currentNode.parent.rightChild = child
                child.parent = currentNode.parent
                child.parent.balanceFactor+=1
                self.DeleteUpdateBalance(currentNode.parent)
            else :                            #当前节点是根节点，直接替换成子节点
                currentNode.replaceNodeData(child.key,
                                           child.payload,
                                           child.leftChild,
                                           child.rightChild)
    def display(self):
        print_t(self.root, label=lambda x:"{}:{}".format(x.key, x.balanceFactor))
                
if __name__ == "__main__":
    tree = AVL()
    """
    tree.put(1)
    tree.put(2)
    tree.display()
    tree.put(30)
    tree.put(40)
    tree.put(50)
    tree.put(60)
    tree.put(70)
    tree.put(80)
    tree.put(0)
    tree.put(25)
    tree.put(35)
    tree.put(21)
    tree.display()
    del tree[40]
    tree.display()
    del tree[30]
    tree.display()
    """
    
    command = input().split()
    while command[0] != 'exit':
        if command[0] == 'put':
            tree.put(int(command[1]))
        elif command[0] == 'delete':
            print("delete()用的是BST的哦，不能保持平衡哦！")
            tree.delete(int(command[1]))
        elif command[0] == 'display':
            tree.display()
        command = input().split()
        