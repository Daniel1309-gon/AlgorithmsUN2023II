def max_pairwise_product():
    n = int(input())
    valores = input().split()

    max1 = 0
    max2 = 0

    for i in valores:
        if int(i) > max1:
            max2 = max1
            max1 = int(i)
        elif int(i) > max2:
            max2 = int(i)

    return max1 * max2

max_pairwise_product()