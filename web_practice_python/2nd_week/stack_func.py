#push : 리스트를 인자로 받아 push한 후 리스트를 리턴하는 함수
def push(myList):

    stack = list()
    top = -1

    for i in myList:
        top +=1
        stack.insert(top,i)
        #print("push :", stack)
    return stack

#pop : 리스트를 인자로 받아 pop한 후 리스트를 리턴하는 함수
def pop(stack):

    top = len(stack)-1
    stack.pop(top)

    return stack
    # while True:
    #     print("pop :", stack)
    #     stack.pop(top)
    #     top-=1

    #     if top <0:
    #         return stack

#list_stack : 스택 출력 함수
def list_stack(stack):
    print("list_stack :", stack, "\n")



myList = [1,5,20,6,2,10]
stack = list()

stack = push(myList)
list_stack(stack)
stack = pop(stack)
list_stack(stack)