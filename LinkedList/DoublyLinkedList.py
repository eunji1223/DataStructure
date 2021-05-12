class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node() # create an empty list with only dummy node

	def __iter__(self):
		v = self.head.next
		while v != self.head:
			yield v
			v = v.next
	def __str__(self):
		return " -> ".join(str(v.key) for v in self)

	def printList(self):
		v = self.head.next
		print("h -> ", end="")
		while v != self.head:
			print(str(v.key)+" -> ", end="")
			v = v.next
		print("h")

	def splice(self,a,b,x):
		if a == None or b == None or x == None:
			return None
		a.prev.next = b.next
		b.next.prev = a.prev
		
		x.next.prev = b
		b.next = x.next
		x.next = a
		a.prev = x
	
	def moveAfter(self,a,x):
		self.splice(a,a,x)
		
	def moveBefore(self,a,x):
		self.splice(a,a,x.prev)
		
	def insertAfter(self,a,key):
		res = self.search(a)
		new_node = Node(key)
		if a == self.head or a == self.head.prev:
			curr = self.head
			while curr != None:
				if curr.key == a.key:
					break
				curr = curr.next
			new_node.next = curr.next
			curr.next.prev = new_node
			curr.next = new_node
			new_node.prev = curr
		elif res == None:
			pass
		else:
			curr = self.head
			while curr != None:
				if curr.key == res:
					break
				curr = curr.next
			new_node.next = curr.next
			curr.next.prev = new_node
			curr.next = new_node
			new_node.prev = curr
			
	def insertBefore(self,a,key):
		res = self.search(a)
		new_node = Node(key)
		if a == self.head or a == self.head.prev:
			curr = self.head
			while curr != None:
				if curr.key == a.key:
					break
				curr = curr.next
			new_node.prev = curr.prev
			curr.prev.next = new_node
			curr.prev = new_node
			new_node.next = curr
		elif res == None:
			pass
		else:
			curr = self.head
			while curr != None:
				if curr.key == res:
					break
				curr = curr.next
			new_node.prev = curr.prev
			curr.prev.next = new_node
			curr.prev = new_node
			new_node.next = curr
			
	def pushFront(self,key):
		self.insertAfter(self.head,key)
		
	def pushBack(self,key):
		self.insertBefore(self.head,key)
		
	def deleteNode(self,x):
		if x == None or x == self.head:
			pass
		elif x == self.head.prev or x == self.head.next:
			x.prev.next = x.next
			x.next.prev = x.prev
		else:
			curr = self.head
			while curr.next != self.head:
				if curr.key == x:
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
					break
				curr = curr.next
			if curr.key == x:
				curr.prev.next = curr.next
				curr.next.prev = curr.prev
				
	def popFront(self):
		if self.head.next == self.head:
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key
		
	def popBack(self):
		if self.head.prev == self.head:
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
		
	def search(self,key):
		curr = self.head.next
		while curr.next != self.head:
			if curr.key == key:
				return key
			curr = curr.next
		if curr.key == key:
			return key
		return None
		
	def isEmpty(self):
		if self.head.next == self.head:
			return True
		return False
		
	def first(self):
		if self.isEmpty():
			return None
		return self.head.next.key
		
	def last(self):
		if self.isEmpty():
			return None
		return self.head.prev.key
	
	def findMax(self):
		if self.head.next == self.head:
			return None
		else:
			curr = self.head.next
			currentMax = -9999
			while curr.next != self.head:
				if currentMax <= curr.key:
					currentMax = curr.key
				curr = curr.next
			if currentMax <= curr.key:
				currentMax = curr.key
			return currentMax
		
	def deleteMax(self):
		if self.head.next == self.head:
			return None	
		Max = self.findMax()
		Max_s = self.search(Max)
		self.deleteNode(Max_s)
		return Max
	
	def size(self):
		count = 0
		curr = self.head.next
		while curr != self.head:
			count+=1
			curr=curr.next
		return count
	
	def sort(self):
		li = []
		while(True):
			a = self.size()
			if a == 0:
				break
			num = self.deleteMax()
			li.append(num)
		for i in range(len(li)):
			self.pushFront(li[i])
		return self

L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
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
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")