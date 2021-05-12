import random, time

def unique_n2(A) :
    for i in range(0, n, 1):
        for j in range(i+1, n-1, 1):
            if A[i] == A[j] :
                print("NO")
            else :
                print("YES")
                break
        break

def unique_nlogn(A) :
    for i in range(0, n, 1):
        A.sort()
        k = i + 1
        while k < n :
            if A[i] == A[k] :
                return("NO")
            k+=1
    print("YES")

def unique_n(A) :
    B = list()
    for i in range(-n, n+1, 1) :
        B.append(i)
    complement = list(set(B) - set(A))
    if len(complement) == n+1 :
        print("YES")
    else :
        print("NO")
			

# input: 값의 개수 n
n = int(input()) 
# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
A = random.sample(range(-n, n+1), n)

s1 = time.process_time()
unique_n2(A)
e1 = time.process_time()
print(int((e1-s1)*10000000)/10000000)

s2 = time.process_time()
unique_nlogn(A)
e2 = time.process_time()
print(int((e2-s2)*10000000)/10000000)

s3 = time.process_time()
unique_n(A)
e3 = time.process_time()
print(int((e3-s3)*10000000)/10000000)