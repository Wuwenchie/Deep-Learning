#輸出九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (i, j, i*j), end = '\t')
    print()

#判斷質數
from math import sqrt
num = int(input('please enter a integer : '))
cal = int(sqrt(num))
is_prime = True
for x in range(2, cal+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d is prime number' % num)
else:
    print('%d is not prime number' % num)                    
#輸入兩個數字 計算最大公倍數和最小公倍數
num_1 = int(input('please enter the first number : '))
num_2 = int(input('please enter the second number : '))
if num_1 > num_2:
    num_1, num_2 = num_2, num_1
for factor in range(num_1, 0, -1):
    if num_1 % factor == 0 and num_2 % factor == 0:
        print('the highest common factor of %d and %d is %d' % (num_1, num_2, factor))
        print('the least common multiple of %d and %d is %d' % (num_1, num_2, num_1*num_2 // factor))
        break
"""
#畫出三角形
num = int(input('please enter the heigh of triangle : '))
for i in range(num):
    for j in range(i + 1):
        print('*', end = '')
    print()

for i in range(num):
    for j in range(num - i - 1):
        print(' ', end = '')
    for j in  range(i + 1):    
        print('*', end = '')
    print()
            

for i in range(num):
    for j in range(num - i -1):
        print(' ', end ='')
    for j in range(2 * i + 1):    
        print('*', end = '')
    print()            