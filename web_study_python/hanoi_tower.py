import stack_class

topA = stack_class.stack_class()
topB = stack_class.stack_class()
topC = stack_class.stack_class()   

def move(A,B):
    
    if B.empty():
        B.push(A.top())
        A.pop()
    else:
        if A.top() > B.top():
            print("이동이 불가능합니다.")
            return 0
        else:
            B.push(A.top())
            A.pop()
    return B.size()

def match(A,B):
    if A =="A":
        if (B=="B"):
            return move(topA,topB)
        else:
            return move(topA,topC)
    elif A=="B":
        if (B=="A"):
            return move(topB,topA)
        else:
            return move(topB,topC)
    else:
        if (B=="A"):
            return move(topC,topA)
        else:
            return move(topC,topB)

if __name__ == "__main__":
    cnt= int(input("원판의 개수를 입력하시오 : "))
    s_cnt = cnt
    while cnt!=0:
        topA.push(cnt)
        cnt -=1

    topA.print_stack()
    while True:
        A, B = input("\n3개의 기둥 A, B, C 가 있습니다.\n1)옮기고자 하는 원판이 있는기둥과 2)원판의 목적지가 될 기둥을 순서대로 입력하시오 ex, A C : ").split()

        if match(A, B) == s_cnt:
            print("성공!")
            break

        topA.print_stack()
        topB.print_stack()
        topC.print_stack()

