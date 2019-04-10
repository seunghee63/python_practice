def Fibonacci(num):
    i = 0; #n-1값을 저장
    step = 1; #step은 n-2값
    cnt = i+step; #출력 수열 값

    while cnt < num:
        if  i == 0 :
            print(1)
            i +=1
            continue

        print(cnt)
        print("i:",i, " step:",step, "cnt:", cnt)

        step = i
        i = cnt
        cnt = i+step

#출력하는 수열의 인덱스를 n 라고 할 때
#n-1 값을 저장하는 변수 i
#n-2 값을 저장하는 변수 step

num = int(input("Enter the number: "))

Fibonacci(num)