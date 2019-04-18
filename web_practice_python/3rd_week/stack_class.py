class stack_class:

    def __init__(self):
        self.__stack_list = list()
        self.__isVariable = False
        self.__top = -1
    
    @property
    def isVariable(self):
        return self.__isVariable

    @isVariable.setter
    def isVariable(self, new_isVar):
        self.__isVariable = new_isVar       

    def push(self, value):

        if self.__isVariable !=False and self.__isVariable == self.__top+1:
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
        return self.__stack_list[self.__top]

    def size(self):
        return len(self.__stack_list)

    def empty(self):
        if len(self.__stack_list) <= 0 :
            return True
        else :
            return False

    def print_stack(self):
        print(self.__stack_list)
    
if __name__ == "__main__":
    stack = stack_class()

    stack.isVariable = 2

    stack.push(1)
    stack.push(1)
    stack.push(1)

    stack.pop()
    stack.pop()

    stack.push(2)
    print(stack.empty())

    stack.push(2)    
    print(stack.top())
    stack.pop()

    stack.push(4)
    print(stack.size())
    stack.pop()
    stack.pop()
    stack.empty()

