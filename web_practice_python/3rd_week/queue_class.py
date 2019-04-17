class queue_class:
    
    def __init__(self):
        self.__queue_list = list()
        self.__isVariable = False
        self.__queue_len = 0
    
    @property
    def isVariable(self):
        return self.__isVariable

    @isVariable.setter
    def isVariable(self, new_isVar):
        self.__isVariable = new_isVar

        if(new_isVar == True):
            a = int(input("큐의 크기를 입력하세요 단, 큐의 크기는 0 이상 "))
            self.__queue_len = a

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

        print("길이 : ",len(self.__queue_list),"제한: ",self.__queue_len)

        if self.__isVariable == True and len(self.__queue_list) == self.__queue_len:
            print("* 더이상 삽입이 불가능합니다.")
            return

        self.__queue_list.append(value)
        return 

    def front(self):
        cnt = len(self.__queue_list)
        if cnt == 0 :
            return 
        print("* front : ",self.__queue_list[0])

    def back(self):
        cnt = len(self.__queue_list)
        if cnt == 0 :
            return 
        print("* back : ",self.__queue_list[cnt-1])

    def size(self):
        print("* size : ",len(self.__queue_list))
        
    def empty(self):
        if len(self.__queue_list) <= 0 :
            print("* 비어있는 queue입니다.")
        else :
            print("* 비어있는 queue가 아닙니다.")
        return

if __name__ == "__main__":
    queue = queue_class()

    queue.isVariable = True

    queue.push(1)
    queue.push(2)
    queue.push(3)

    queue.empty()
    queue.front()
    queue.back()

    queue.push(4)
    queue.back()

    queue.pop()
    queue.pop()
    queue.pop()

    queue.empty()
    queue.size()
    queue.front()