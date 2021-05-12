class myList():
	def __init__(self):
		self.capacity = 2	  # myList의 용량 (저장할 수 있는 원소 개수)
		self.n = 0          # 실제 저장된 값의 개수
		self.A = [None] * self.capacity # 실제 저장 자료구조 (python의 리스트 사용) 

	def __len__(self):
		return self.n
	
	def __str__(self):
		return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'
	def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		try:
			if k >= self.n:
				raise IndexError
			return self.A[k]
		except:
			raise IndexError
		

	def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		try:
			if k < 0 & k >= -(self.capacity):
				pass
			elif k>=0 & k < self.capacity:
				pass
			else:
				raise IndexError
			self.A[k] = x
		except:
			raise IndexError
		
	def size(self):
		return len(self.A)

	def changing_size(self, new_capacity):
		print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
		B = list()      # 1. new_capacity의 크기의 리스트 B를 만듬
		for j in range(0,new_capacity,1):
			B.append(0)
		for i in range(0,self.n,1):       # 2. self.A의 값을 B로 옮김
			B[i] = self.A[i]
		del self.A                    # 3. del self.A  (A 지움)
		self.A = B                    # 4. self.A = B
		self.capacity = new_capacity  # 5. self.capacity = new_capacity
	
	def append(self, x):
		if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
			self.changing_size(self.capacity*2)
		self.A[self.n] = x     # 맨 뒤에 삽입
		self.n += 1            # n 값 1 증가

	def pop(self, k=None): # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴, None의 값이 -1로 되어있음
		if k >= 0:	
			if k < self.n:         # 빈 리스트이거나 올바른 인덱스 범위를 벗어나면: 
				pass
			else:
				raise IndexError
		else :
			if k >= -(self.n):
				pass
			else:
				raise IndexError
			
		if self.capacity >= 4 and self.n <= self.capacity//4: # 실제 key 값이 전체의 25% 이하면 halving
			self.changing_size(self.capacity//2)
		if k < 0 :  # 1. k 값이 주어진 경우와 주어지지 않은 경우 구별해야 함, None의 값이 -1로 되어있음
			k += self.n
		x = self.A[k]  # 2. x = self.A[k]
		for i in range(k, self.n-1 , 1):
			self.A[i] = self.A[i+1]	      # 3. A[k]의 오른쪽의 값들이 한 칸씩 왼쪽으로 이동해 메꿈
		self.n -= 1                     # 4. self.n -= 1
		return x                        # 5. return x
	
	def insert(self, k, x):
		if k >= 0:
			if k >= self.n:# k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
				raise IndexError # 1. k의 범위가 올바르지 않으면 IndexError 발생시킴
			pass
		else:
			if k < -self.n:      # 주의: k 값이 음수값일 수도 있음 
				raise IndexError 
			pass
				
		if self.n == self.capacity:
			self.changing_size(self.capacity*2)
		                    # 2. self.n == self.capacity이면 self.change_size(self.capacity*2) 호출해 doubling
		if k < 0:
			k += self.n	
		for i in range(self.n-1, k-1, -1) :     # 3. A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
			self.A[i+1] = self.A[i]			
		self.A[k] = x        # 4. self.A[k] = x
		self.n += 1          # 5. self.n += 1
		