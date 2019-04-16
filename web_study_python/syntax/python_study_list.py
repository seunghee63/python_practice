
# coding: utf-8

# In[ ]:



#리스트
#리스트와 문자열 거의 비슷하지만
#리스트는 자료형에 구애받지 않는다는 점이 다름!


# In[17]:

#리스트 생성 및 초기화

#동적으로 데이터 삽입가능
empty_list = []
empty_list = list()


#리스트 생성 및 초기화
a = [1,2,3,4,5]
b = ["a", "b", "c"]
c = ["a", 1, "b", 2]
d = [a, b, c]
#[[1, 2, 3, 4, 5], ['a', 'b', 'c'], ['a', 1, 'b', 2]]


# In[18]:

#리스트 요소 접근

#파이썬 이터러블 객체-> 문자열, 리스트.. 의 공통점 : 인덱싱,슬라이싱 가능
#a[::2] #뒤에 2는 step!

a = [1,2,3,4,5]

print(a[0])
#1

#a[시작:끝:step],디폴트값[맨처음, 맨끝, 1]
print(a[::])
#[1,2,3,4,5]

#마이너스는 리스트의 뒤에서부터 접근.
print(a[-1])
#5
print(a[-2])
#4
print(a[-3])
#3


# In[69]:

#-1
a = [1,2,3,4,5]
arr = [1,2,3,4,5]

for i in a:
    arr[-i] = a[i-1]
    
print(arr)

arr = list(range(10))
print(arr)
#[0,1,2,3,4,5,6,7,8,9]

#a[시작:끝:step]

arr = list(range(10))
print(arr[::-1])
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
arr = list(range(10))
print(arr[::1])
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr = list(range(10))
print(arr[9:7:-1])
#[9, 8]
arr = list(range(10))
print(arr[7:9:1])
#[7, 8]

arr = list(range(10))
print("3 ) ", arr[1::-1])
#[1, 0]

arr = list(range(10))
print("4 ) ",arr[4:3:-1])
#[4]


# In[20]:

#리스트 안에 리스트가 있을경우, 

d[1][2]


# In[40]:

#shallow copy & deep copy

#shallow copy 
a0 = [1,2,3,4,5]
b0 = a0
b0[0] = 10
#a0[0] == b[0] == 10

#a와 b의 결과값은 같음.
#c의 포인터와 같은 개념! 레퍼런스 아이디!

#deep copy
b0 = a0[:]
b0[0] = 10
#a0[0] != b[0]


# In[43]:

#리스트 함수


# In[76]:

#append

a = [1,2,3,4,5]
a.append(1)
#[1,2,3,4,5,1]

a = [1,2,3,4,5]
a.append([1])
#[1,2,3,4,5,[1]]


# In[79]:

#extend : 여러개를 한꺼번에 추가 가능

a = [1,2,3,4,5]
a.extend([0,2,3,[4,4,5]])
#[1, 2, 3, 4, 5, 0, 2, 3, [4, 4, 5]]

a = [1,2,3,4,5]
a.extend([[4,4,5]])
#[1, 2, 3, 4, 5, [4, 4, 5]]

#+ :extend와 기능은 같으나, extend
a = a+arr


# In[80]:

#reverse

a = [1,2,3,4,5]
a.reverse()
#[5, 4, 3, 2, 1]

print(a)


# In[90]:

#sort

c = [4,2,5,7,8,9,3,2,1]
c.sort()
#[1, 2, 2, 3, 4, 5, 7, 8, 9]

c = [4,2,5,7,8,9,3,2,1]
c.sort(reverse=True)
#[9, 8, 7, 5, 4, 3, 2, 2, 1]


# In[107]:

#remove & insert

arr = list(range(10))


#remove
arr.remove(5)#인자는 인덱스가 아니라 값임!!
print(arr)

#insert : 원하는 위치에 자료 추가 가능 ( <-> append: 맨 뒤에 추가 )
#자료구조 만들 때
arr = list(range(10))

arr.insert(3,100)
print(arr)
#[0, 1, 2, 100, 3, 4, 6, 7, 8, 9]

arr.insert(0,20)
print(arr)
#[20, 0, 1, 2, 100, 3, 4, 6, 7, 8, 9]

#pop : 인덱스 삭제
#자료구조 만들 때
#리스트 섞는 함수 -> 값 하나 추출
c = list(range(10))

c.pop(1) #인덱스
print(c)
#[0, 2, 3, 4, 5, 6, 7, 8, 9]

c.pop()
print(c)
#[0, 2, 3, 4, 5, 6, 7, 8]

c.pop(-1)
print(c)
#[0, 2, 3, 4, 5, 6, 7]


# In[102]:

#remove

arr = list(range(10))
arr.remove(5)#인자는 인덱스가 아니라 값임!!
#[0, 1, 2, 3, 4, 6, 7, 8, 9]
print(arr)


# In[100]:

#arr.remove(5)#인자는 인덱스가 아니라 값임!!
#print(arr)

