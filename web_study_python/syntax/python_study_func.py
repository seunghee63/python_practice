
# coding: utf-8

# In[ ]:



# 반복문 fun


# In[ ]:

def add(a,b):
    return a+b;

#f리턴이 없는 함수는, 프로시져 => 전역변수를 이용해서 값 변경하는 경우에 많이 사용됨

#프로시저는 변수에 값을 할당하면 안됨.


# In[ ]:

#namespace

#local 지역변수


#global 전역변수
#상수와 비슷한 느낌..
#지역변수에서 전역변수값을 바꾸고 싶을 때는, global a , a = 3
a =3
def add(a,b):
    global a = 2;
    return a+b;

#built-in 내장변수
#__init__, ...


# In[1]:

def sub1(a,b):
    return a-b

def sub2(a,b):
    print(a-b)
    
print(sub1(1,2))
sub2(1,2)


# In[19]:

a = 5

def sub1(a,b):
    global a
    a = 3
    return a-b

print(sub1(7,1))


# In[18]:

import this
#import가 되는지 test하기 위한 기본 라이브러리


# In[ ]:

def add(a,b):
    return a+b;

def sub1(a,b):
    return a-b

