stack_list = list()
top = -1

#1) while문으로 숫자를 입력 받아 리스트에 저장(저장 순서는 스택, 큐에 따라서 다름)

while True:

    n_node = input("insert : ")

    if n_node != "":
        top +=1
        stack_list.insert(top,int(n_node))
    else:
        break

print("input :", stack_list, "top :", top,)
print()


#2) 리스트의 크기만큼 while문을 돌려서 데이터 출력(각 자료구조의 특성에 맞게), 출력시에는 값을 출력함과 동시에 리스트에서 해당요소가 삭제되어야함.

while True:

    if top >= 0:
        print("pop :",stack_list[top])
        stack_list.pop(top)
        top-=1
    else :
        break

print("result :", stack_list, "top :", top)
