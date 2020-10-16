def my_max_pairwise_product(numbers):
    n = len(numbers)

    max_1 = numbers[0]
    index1 = 0
    
    for i in range(1,n):
        if max_1 < numbers[i]:
            max_1 = numbers[i]
            index1 = i

    if index1 == 0:
        max_2 = numbers[1]
        index2 = 1
        for j in range(1,n):
            if  max_2 < numbers[j]:
                max_2 = numbers[j]
                index2 = j
    else:
        max_2 = numbers[0]
        index2 = 0
        for j in range(n):
            if j != index1 and max_2 < numbers[j]:
                max_2 = numbers[j]
                index2 = j
    return numbers[index1]*numbers[index2]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(my_max_pairwise_product(input_numbers))