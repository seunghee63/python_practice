
# coding: utf-8

# In[5]:




# In[6]:

a = "Hello!"
b = "Nice to meet you"


# In[17]:

#find
#리턴값 : 처음문자열이 나온 위치
#없을 경우 : -1

a = "Hello! World"
a.find("a")
#-1

b = "Hello!"
a.find(b)
#0

c = "World"
a.find(c)
#7


# In[14]:

#join : 문자열 이터레블 객체에 사용

c = "HELLO!"
" ".join(c)
#c = "H E L L O !"

d = "문자열"
"_ ".join(d)
#d = "문_ 자_ 열"

e = "1"
"ㅎ".join(e)
#e = "1"


#많이 사용되지는 않음. 사용될 경우는.. 파일 경로 같은 경우?


# In[ ]:

#upper & lower

#a= a.upper
#a= a.lower

#넣어줘야 바뀜!


# In[23]:

#replace

a = "HELLO!"
a.replace("H","b")
#a 변화 없음-> 마찬가지로 바꾼 값을 저장 해 주어야 함
a=a.replace("H","b")
#a = "bELLO!"

b = "Ice Coffee"
b = b.replace("H","ㅎㅎ")
#변화 없음
b = b.replace("ce"," love")
#b = "I love Coffee"

#바꾼 값을 return 해줌
print(b)


# In[7]:

#split

"안녕 반가워 네 이름은 뭐니?".split(" ")
#['안녕', '반가워', '네', '이름은', '뭐니?']

"안녕 반가워 네 이름은 뭐니?".split()
#['안녕', '반가워', '네', '이름은', '뭐니?']

#split의 인자가 아무것도 없을 경우에는, 자동으로 공백 기준으로 분리


# In[38]:

#count

"안녕 반가워 네 이름은 뭐니?".count(" ")
#4
"ㅎ".count("   ")
#2


# In[26]:

#startswith : 문자열이 무엇으로 시작하는지 파악하는 함수

"apple".startswith("a")
#true

"apple".startswith("ap")
#false

"apple".startswith("p")
#false

#return: boolean
#제어문에서 사용


# In[ ]:



