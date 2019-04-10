queue_list = list()

#1) while문으로 숫자를 입력 받아 리스트에 저장(저장 순서는 스택, 큐에 따라서 다름)
print("더 이상 원소를 추가하고 싶지 않을 경우, '엔터'")
while True:

    n_node = input("enqueue : ",)

    if n_node != "":
        queue_list.append(int(n_node))
    else:
        break


print("*queue : ", queue_list)
print()


#2) 리스트의 크기만큼 while문을 돌려서 데이터 출력(각 자료구조의 특성에 맞게), 출력시에는 값을 출력함과 동시에 리스트에서 해당요소가 삭제되어야함.

while True :
    i=0;

    print("dequeue : ", queue_list[i])
    queue_list.pop(i)

    #마지막일 때
    if(0==len(queue_list)):
        break

print("*queue :" , queue_list)