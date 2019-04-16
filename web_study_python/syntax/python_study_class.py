
# coding: utf-8

# In[1]:

#self object만의 값


# In[3]:

class Person:
    # class Person의 멤버변수
    name = "홍길동"
    number = "01077499954"
    age = "20"
 
    # class Person의 메소드
    def info(self):
        print("제 이름은 " + self.name + "입니다.")
        print("제 번호는 " + self.number + "입니다.")
        print("제 나이는 " + self.age + "세 입니다.")
 
if __name__ == "__main__":# main namespace를 의미합니다.
    customer = Person()#Person의 객체 customer 생성
    customer.info()#info 함수 호출
 


# In[4]:

class Person:
    # class Person의 멤버변수
    # __(double underscore)
    # __는 클래스외부에서 클래스 멤버에 접근하지 못하게 하기위함
    __name = "홍길동"
    __number = "01077499954"
    __age = "20"
 
    @property  #property 값을 갖고 옴
    def name(self):
        return self.__name
 
    @name.setter #setter 값을 바꿔줌
    def name(self, newName):
        self.__name = newName
 
    # class Person의 메소드
    def info(self):
        print("제 이름은 " + self.__name + "입니다.")
        print("제 번호는 " + self.__number + "입니다.")
        print("제 나이는 " + self.__age + "세 입니다.")
 
if __name__ == "__main__":# main namespace를 의미합니다.
    customer = Person()#Person의 객체 customer 생성
    customer.info()#info 함수 호출
    print(customer.name)
    customer.name="이태일"
    print(customer.name)
    
#    __gkgk__ : 매직메소드


# In[27]:

class Person : 
    def __init__(self, name):
        self.__name = name
    
    #def setname(self, newName):
     #   self.name = newName
    
    @property
    def name(self):
        return self.__name
 
    @name.setter
    def name(self, newName): 
        self.__name = newName
    
if __name__ == "__main__":
    p1 = Person("양승희")
    p2 = Person("양승희")
    p1.name="홍길동"
    
    print (p1.name)
    print (p2.name)
    


# In[30]:

#이터레이터

#매직메소드
#__iter__
#__next__

class Fibo :
    def __init__(self) : 
        self.prv = 0
        self.cur = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.cur, self.prv = self.cur + self.prv , self.cur
        return self.prv
    
f = Fibo()
for i in range(10):
    print(next(f))


# In[31]:

#yield 반환값. yield를 만나면 ajacna => 제너레이터. 리터레이터화가됨.(셀수있는집합)

def fib():
    prv = 0
    cur = 1
    
    while 1:
        yield cur
        cur, prv = cur+prv, cur
        
f = fib()
for i in range(10):
    print(next(f))
    
#따로 next를 정의 해 주지 않아도 됨


# In[ ]:

#클래스

