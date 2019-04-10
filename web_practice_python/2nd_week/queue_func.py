# enqueue : 리스트를 인자로 받아 enqueue한 후 리스트를 리턴하는 함수
def enqueue(myList):
    queue = list()
    for i in myList:
        queue.append(i)
        print("enqueue : ", queue)
    
    return queue

# dequeue : 리스트를 인자로 받아 dequeue한 후 리스트를 리턴하는 함수
def dequeue(queue):
    
    for i in range(len(queue)) :
        queue.pop(0)
        print("dequeue : ", queue)
    
    return queue

# list : 큐를 출력하는 함수 
def list_queue(queue):
    print("list_queue :", queue, "\n")



myList = [1,5,20,6,2,10]
queue = list()

queue = enqueue(myList)
list_queue(queue)
queue = dequeue(queue)
list_queue(queue)