list = [ 7, 4, 5, 3, 1]

round = 1

while round < len(list):
    min = list[round-1]

    i = round
    while i < len(list):
        if min > list[i]:
            min = list[i]
            min_index = i
        i+=1

    tmp = list[round-1]
    list[round-1] = min
    list[min_index] = tmp

    print(round , "round : ", list)
    round +=1

print("\nresult : ",list)
