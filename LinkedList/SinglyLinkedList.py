class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		new_node = Node(key)
		new_node.next = self.head
		self.head = new_node
		self.size+=1
		
	def pushBack(self, key):
		new_node = Node(key)
		if self.size == 0:
			self.head = new_node
		else:
			tail = self.head
			while tail.next != None:
				tail = tail.next
			tail.next = new_node
		self.size += 1
		
	def popFront(self): 
		key = None
		if len(self)>0:
			key = self.head.key
			self.head = self.head.next
			self.size-=1
		return key
		# head 노드의 값 리턴. empty list이면 None 리턴
	def popBack(self):
		if self.size == 0:
			return None
		else:
			prev = None
			cur = self.head
			while cur.next != None:
				prev = cur
				cur = cur.next
			tail = cur
			key = tail.key
			if prev == None:
				self.head = None
			else:
				prev.next = tail.next
			self.size -= 1
			return key
		# tail 노드의 값 리턴. empty list이면 None 리턴
	def search(self, key):
		s = self.head
		while s:
			if s.key == key:
				return s
			s = s.next
		return None
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		
	def remove(self, x):
		if x == None:
			return False
		elif x == self.head:
			if self.head.next == None:
				self.head = None
				self.size-=1
				return True
			else:
				self.head = self.head.next
				self.size-=1
				return True
		else:
			prev = None
			cur = self.head
			while cur != None:
				if cur == x:
					prev.next = cur.next
					self.size-=1
					return True
				else:
					prev = cur
					cur = cur.next
			return False
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		# x는 key 값이 아니라 노드임에 유의!
	def reverse(self, key):
		A = self.search(key)
		if A == None:
			pass
		else:
			prev = None
			curr = self.head
			while curr != None:
				if key == self.head.key:
					cut = []
					count = self.size
					while curr != None:
						cut.append(curr)
						curr = curr.next
					self.head = cut.pop()
					curr = self.head
					while len(cut)>0:
						curr.next = cut.pop()
						curr = curr.next
					curr.next = None
						
				elif curr.key == key:
					cut = []
					while curr != None:
						cut.append(curr)
						curr = curr.next
					while len(cut) > 0:
						curr = cut.pop()
						prev.next = curr
						prev = prev.next
					curr.next = None
					break
				prev = curr
				curr = curr.next
	def findMax(self):
		if self.size == 0:
			return None
		else:
			count = self.size
			curr = self.head
			currentMax = -9999
			while count != 0:
				if currentMax <= curr.key:
					currentMax = curr.key
				curr = curr.next
				count-=1
			return currentMax
		# self가 empty이면 None, 아니면 max key 리턴
	def deleteMax(self):
		if self.size == 0:
			return None
		Max = self.findMax()
		Max_s = self.search(Max)
		self.remove(Max_s)
		return Max
		
	def insert(self, k, val):
		if k<0:
			self.pushBack(val)
		else:
			if self.size<k:
				self.pushBack(val)
			elif k == 0:
				self.pushFront(val)
			else:
				new_node = Node(val)
				curr = self.head
				count = 1
				while curr != None:
					if count == k:
						a = new_node
						a.next = curr.next
						curr.next = a
						break
					count+=1
					curr = curr.next
				self.size += 1
			
	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")