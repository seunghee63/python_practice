list = [ 7, 8, 5, 1, 3]

round = 1
i = 0

while round < len(list):

    while True:

        if i == len(list) - 1:
            i = 0
            break

        if list[i] > list[i + 1]:
            tmp = list[i]
            list[i] = list[i + 1]
            list[i + 1] = tmp
        i += 1

    print(round , "round : ", list)

    round += 1

print("\nresult : ",list)
