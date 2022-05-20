def prime(lower, upper):
    list = []
    flag = 0
    for num in range(lower, upper + 1):
        flag = 0
        if num > 1:

            for i in range(2, num):
                if (num % i) == 0:
                    flag = 1
        if flag == 0:
           # print("Odd", num)
            list.append(num)

    return list




print(prime(0,1000))



















