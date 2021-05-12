import time
from collections import OrderedDict
class HashOpenAddr:
	def __init__(self, size):
		self.size = int(size*(3/2))
		self.keys = [None]*self.size
		self.values = [None]*self.size
	def __str__(self):
		s = ''
		for k in self:
			s = s + str(k)
			s += ' '
		return s
	def __iter__(self):
		for i in range(self.size):
			yield self.keys[i]
	
	def find_slot(self,key):
		re = self.hash_function(key)
		start = re
		while self.keys[re] != None and self.keys[re] != key:
			re = self.rehash(re)
			if re == start:
				return None
		return re
		
	def set(self,key,value= None):
		re = self.find_slot(key)
		if re == None: return None
		elif self.keys[re] != None:
			self.values[re] = value
			return key
		else:
			self.keys[re], self.values[re] = key,value
			return key
	
	def rehash(self,hash):
		return (hash+1)%self.size
	
	def hash_function(self,key):
		return key%self.size
	
	def remove(self,key):
		i = self.find_slot(key)
		if i == None: return None
		if self.keys[i] == None: return None
		j = i
		while(True):
			self.keys[i] = None
			self.values[i] = None
			while(True):
				j = self.rehash(j)
				if self.keys[j] == None: return key
				k = self.hash_function(self.keys[j])
				if k<= i <j or i< j <k or j< k <=i:
					break
			self.keys[i] = self.keys[j]
			i = j
	def search(self, key):
		re = self.find_slot(key)
		if re == None: return None
		elif self.keys[re] != None: return key
		else: return None
# 입력
result1 = []
re_result = []
A = [int(x) for x in input().split()]
A1 = HashOpenAddr(len(A))
for i in range(len(A)):
	key = A1.set(A[i])
B = [int(x) for x in input().split()]
B1 = HashOpenAddr(len(B))
for j in range(len(B)):
	key = B1.set(B[j])
for k in range(int(len(B)*(3.2))):
	if A1.search(k) == B1.search(k) and A1.search(k) != None:
		result1.append(A1.search(k))
		A1.remove(k)
start = time.time()
for h in range(len(B)):
	if B[h] in result1 and B[h] in A:
		re_result.append(B[h])
		A.remove(B[h])
print(int(time.time() - start))
print(" ".join(map(str,re_result)))
print(' '.join(map(str,list(OrderedDict.fromkeys(re_result)))))