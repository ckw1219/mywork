#辗转相除法结合

def gcd(input_number):
    n1 = input_number[0]
    n2 = input_number[1]
    current_gcd = 1
    if n1 == n2:
        current_gcd = n1
    elif n1 > n2:
        while n2 != 0:
            mod = n1 % n2
            n1 = n2 
            n2 = mod
        current_gcd = n1
    else:
        while n1 != 0:
            mod = n2 % n1
            n2 = n1
            n1 = mod
        current_gcd = n2
    return current_gcd
if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(gcd(input_numbers))

#输入改进一下
import sys

def gcd(n1,n2):
    current_gcd = 1
    if n1 == n2:
        current_gcd = n1
    elif n1 > n2:
        while n2 != 0:
            mod = n1 % n2
            n1 = n2 
            n2 = mod
        current_gcd = n1
    else:
        while n1 != 0:
            mod = n2 % n1
            n2 = n1
            n1 = mod
        current_gcd = n2
    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))

