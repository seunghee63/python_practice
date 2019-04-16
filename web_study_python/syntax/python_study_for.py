
# coding: utf-8

# In[31]:



# 반복문 for 


# In[32]:

#시퀀스 자료형 : 쪼갤 수 있음
#이터레이션 : 반복문을 이용하여 시퀀스의 요소 접근(하는것을 이터레이팅)

#range(시작,끝,step)
#끝을 10이라고 하면, 실제로는 9까지만 접근함

#for 임시저장할변수 in range();
#in 다음에는 리터레이션 변수가 올 수 있음! range()는 파이썬에서 제공하는 이터레이션 함수. 


# In[33]:

myList =["사과", "딸기", "냠냠냠"]

for each in myList:
    print(each)


# In[34]:

myList =["apple", "banana", "mango","mellon"]
new = myList[:]

for each in myList:
    each = each.upper()
    print(each)


# In[35]:

for i in range(10,0,-1):
    print(i)


# In[36]:

for i in range(1,10,1):
    for j in range(1,10,1):
        #print(i,"*",j,"=", j*i)
        #세번째 인자는 튜플!
        print(str(i) + "*" + str(j) + "=" + str(i*j))
        print("%d * %d = %d"%(i,j,i*j))
    print()
    #print(,end='마지막에 넣고싶은 것')


# In[37]:

#conprohentiosn

nList = [i for i in range(100)]
print(nList)

List = [0 for _ in range(100)]
print(List)


# In[38]:

wordList1 = ["apple", "app", "agile", "aside", "appendix", "ace", "append", "attention" ]
wordList2 = ["duck", "cat", "pizza", "chicken", "elephant", "mouse","fence" ]

wordList = ['apple', 'app', 'agile', 'aside', 'appendix', 'ace', 'append', 'attension', 'age', 'duck', 'cat', 'pizza', 'chicken', 'elephant', 'mouse', 'fence']

#origin
for each in wordList:
    if(each.startswith("a")):
        print(each)

myList = [each for each in wordList if each.startswith('a')]
print(myList)
    


# In[40]:

myList = [i for i in range(1,101) if((i%2)==1)]
print(myList)


# In[41]:

myList = [i for i in range(1,101,2)]
print(myList)


# In[ ]:



