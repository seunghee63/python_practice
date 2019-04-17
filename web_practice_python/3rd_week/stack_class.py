class stack_class:

    def __init__(self):
        self.__stack_list = list()
        self.__isVariable = False
        self.__stack_len = 0
        self.__top = -1
    
    @property
    def isVariable(self):
        return self.__isVariable

    @isVariable.setter
    def isVariable(self, new_isVar):
        self.__isVariable = new_isVar
        
        if(new_isVar == True):
            a = int(input("스택의 크기를 입력하세요 단, stack의 크기는 0 이상 "))
            self.__stack_len = a

    def push(self, value):

        if self.__isVariable == True and self.__stack_len == self.__top+1:
            print("* 더이상 삽입이 불가능합니다.")
            return 
        
        self.__top +=1
        self.__stack_list.insert(self.__top,value)
        return 

    def pop(self):
        if self.__top == -1:
            print("* 더이상 삭제가 불가능합니다.")
            return 

        self.__stack_list.pop(self.__top)
        self.__top -=1 
        return 

    def top(self):
        print("* top value: ",self.__stack_list[self.__top])

    def size(self):
        print("* size : ",len(self.__stack_list))

    def empty(self):
        if len(self.__stack_list) <= 0 :
            print("* 비어있는 stack입니다.")
        else :
            print("* 비어있는 stack이 아닙니다.")
        return
    
if __name__ == "__main__":
    stack = stack_class()

    stack.isVariable = True

    stack.push(1)
    stack.push(1)
    stack.push(1)

    stack.pop()
    stack.pop()

    stack.push(2)
    stack.empty()
    stack.push(2)    
    stack.top()
    stack.pop()
    stack.push(4)
    stack.size()
    stack.pop()
    stack.pop()
    stack.empty()

