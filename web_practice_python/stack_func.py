

#리스트를 인자로 받아 push한 후 리스트를 리턴
def push(myList):

    stack = list()
    top = -1

    for i in myList:
        top +=1
        stack.insert(top,i)
        print("input :", stack, " top :", top,)
    
    print()
    return stack

#리스트를 인자로 받아 pop한 후 리스트를 리턴
def pop(stack):

    top = len(stack)-1
    
    while True:
        print("pop :",stack[top])
        stack.pop(top)
        top-=1

        if top <0:
            return stack



myList = [1,5,20,6,2,10]
stack = list()

stack = push(myList)
print("push_result: ",stack)

stack = pop(stack)
print("pop_result: ",stack)
