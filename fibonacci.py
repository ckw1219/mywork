def fibonacci(numbers):
    if numbers == 0:
        return 0
    elif numbers == 1:
        return 1
    else:
        n = numbers+1
        f = [0 for i in range(n)]
        f[1] = 1
        for i in range(2,n):
             f[i] = f[i-1]+f[i-2]
        return f[numbers]    

if __name__ == '__main__':
    n = int(input())
    print(fibonacci(n))


