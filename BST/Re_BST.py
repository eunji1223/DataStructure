# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):
        if v:
            print(v.key, end=" ")
            self.preorder(v.left) # 재귀
            self.preorder(v.right)

    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v.key, end=" ")
            self.inorder(v.right)

    def postorder(self, v):
        if v:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end = " ")

    def find_loc(self, key):  # if key is in T, return its Node
        # if not in T, return the parent node under where it is inserted
        if self.size == 0: return None
        p = None  # p = parent node of v
        v = self.root
        while v:  # while v != None
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left

        return p

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:  # p is parent of v
                if p.key < key:
                    p.right = v
                else:
                    p.left = v
                v.parent = p
            self.Update(v)
        self.size += 1
        return v
	# key가 이미 트리에 있다면 에러 출력없이 None만 리턴!

    def deleteByMerging(self, x): 
        # assume that x is not None
        if x == None:return None
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b
        else:  # a != None
            c = m = a
            # find the largest leaf m in the subtree of a
            while m.right:
                m = m.right
            m.right = b
            if b: b.parent = m

        if self.root == x:  # c becomes a new root
            if c:
                c.parent = None
                self.root = c
        else:  # c becomes a child of pt of x
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c: c.parent = pt
        self.Update(b)
        self.size -= 1

    def deleteByCopying(self, x):
        pt, L, R = x.parent, x.left, x.right
        if L: # L이 있음
            y = x.left # L = x.left
            while y.right:
                y = y.right
            x.key = y.key
            if y.left:
                y.left.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.left
            else:
                y.parent.right= y.left
            search = y.parent
            del y
            self.Update(search)
            self.size -= 1
            return L

        elif not L and R: # R만 있음
            y = R
            while y.left:
                y = y.left
            x.key = y.key
            if y.right:
                y.right.parent = y.parent
            if y.parent.left is y:
                y.parent.left = y.right
            else:
                y.parent.right = y.right
            search = y.parent
            del y
            self.Update(search)
            self.size -= 1
            return R

        else: # L도 R도 없음
            if pt == None: # x가 루트노드인 경우
                self.root = None
            else:
                if pt.left is x:
                    pt.left = None
                else:
                    pt.right = None
            del x
            self.Update(pt)
            self.size -= 1
            return pt
        


    def height(self, x): # 노드 x의 height 값을 리턴
        if x == None: return -1
        else: return x.height
        
        
    def Update(self,x):
        if x == None:return None
        while x:
            if x:
                if x.left != None:
                    if x.right != None:
                        x.height = max(x.left.height, x.right.height) + 1
                    else:
                        x.height = x.left.height + 1
                elif x.right != None:
                    if x.left != None:
                        x.height = max(x.left.height, x.right.height) + 1
                    else:
                        x.height = x.right.height + 1
                else:
                    x.height = 0
            x = x.parent

    def succ(self, x):
        if self.find_loc(x.key) == None or x == None:
            return None
        num = x.parent
        pt = x
        j = x.right
        if x.right:
            if x.right.left:
                while j != None:
                    x = j
                    j = j.left
                return x
            else:
                return x.right
        else:
            if x.parent and x.parent.left:
                if x.parent.left == x:
                    return x.parent
                else:
                    while num != None:
                        if x.key < num.key:
                            return num
                        num = num.parent
                    if num == None:
                        return None
                    else:
                        return None
		# key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
		# x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴

    def pred(self, x):
        if self.find_loc(x.key) == None or x == None:
            return None
        num = x.parent
        pt = x
        j = x.left
        if x.left:
            if x.left.right:
                while j != None:
                    x = j
                    j = j.right
                return x
            else:
                return x.left
        else:
            if x.parent and x.parent.right:
                if x.parent.right == x:
                    return x.parent
                else:
                    while num != None:
                        if x.key > num.key:
                            return num
                        num = num.parent
                    if num == None:
                        return None
            else:
                return None
		# key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
		# x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴

    def rotateLeft(self, z):
            # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
            x = z.right
            if x == None:
                return None
            b = x.left
            x.parent = z.parent
            if z.parent:
                if z.parent.left == z:
                    z.parent.left = x
                else:
                    z.parent.right = x
            if x: x.left = z
            z.parent = x
            z.right = b
            if b: b.parent = z
            if z==self.root and z!=None:
                self.root = x
            self.Update(z)
	
		
    def rotateRight(self, z):
        # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        x = z.left
        if x == None:
            return None
        b = x.right
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        if x: x.right = z
        z.parent = x
        z.left = b
        if b: b.parent = z
        if z == self.root and z!=None:
            self.root = x
        self.Update(z)
			
	
T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
