def Fibonacci(num):
    step = 0; #n-2값을 저장
    i = 1; #n-1
    cnt = i+step; #출력 수열 값

    while cnt < num:
        if  step == 0 :
            print(1)
            print("i:",i, " step:",step, " cnt:", cnt)
            step +=1
            continue

        print(cnt)
        print("i:",i, " step:",step, "cnt:", cnt)

        i = step
        step = cnt
        cnt = i+step

#출력하는 수열의 인덱스를 n라고 할 때, 
#n-2 값을 저장하는 변수 step
#n-1 값을 저장하는 변수 i

num = int(input("Enter the number: "))

Fibonacci(num)