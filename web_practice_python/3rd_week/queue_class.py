class queue_class:
    
    def __init__(self):
        self.__queue_list = list()
        self.__isVariable = False
    
    @property
    def isVariable(self):
        return self.__isVariable

    @isVariable.setter
    def isVariable(self, new_isVar):
        self.__isVariable = new_isVar
            
    def info(self):
        print(self.__queue_list)
        print(self.__isVariable)

    def pop(self):    
        cnt = len(self.__queue_list)

        if cnt == 0:
            print("* 더이상 삭제가 불가능합니다.")
            return 

        self.__queue_list.pop(0)

    def push(self, value):

        if self.__isVariable != False and len(self.__queue_list) == self.__isVariable:
            print("* 더이상 삽입이 불가능합니다.")
            return

        self.__queue_list.append(value)

    def front(self):
        if len(self.__queue_list) == 0 :
            return 

        return self.__queue_list[0]

    def back(self):
        cnt = len(self.__queue_list)
        if cnt == 0 :
            return 
        return self.__queue_list[cnt-1]

    def size(self):
        return len(self.__queue_list)
        
    def empty(self):
        if len(self.__queue_list) <= 0 :
            return True
        else :
            return False

if __name__ == "__main__":
    queue = queue_class()


    queue.push(1)
    queue.isVariable = 2

    queue.push(2)
    queue.push(3)

    queue.empty()
    print(queue.front())
    print(queue.back())


    queue.push(4)
    queue.push(4)
    queue.push(4)
    queue.back()

    queue.pop()
    queue.pop()
    queue.pop()

    queue.empty()
    queue.size()
    queue.front()