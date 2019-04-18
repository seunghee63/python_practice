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
        
        if new_isVar == False:
            self.__stack_len = 0

    @property
    def stack_len(self):
        return self.__stack_len

    @stack_len.setter
    def stack_len(self,new_len):
        self.__stack_len = new_len
        

    def push(self, value):

        if self.__isVariable == True and self.__stack_len == self.__top+1:
            print("* 더이상 삽입이 불가능합니다.")
            return 
        
        self.__top +=1
        self.__stack_list.insert(self.__top,value)

    def pop(self):
        if self.__top == -1:
            print("* 더이상 삭제가 불가능합니다.")
            return 

        self.__stack_list.pop(self.__top)
        self.__top -=1 

    def top(self):
        print("* top value: ",self.__stack_list[self.__top])

    def size(self):
        print("* size : ",len(self.__stack_list))

    def empty(self):
        if len(self.__stack_list) <= 0 :
            return True
        else :
            return False
    
if __name__ == "__main__":
    stack = stack_class()

    stack.isVariable = True
    stack.stack_len = 2

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

