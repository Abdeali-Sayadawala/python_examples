# -*- coding: utf-8 -*-

def sum_of_squares(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + (i*i)
    return sum

def square_of_sum(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + i
    sum = sum**2
    return sum

num = int(input())
ans = max(sum_of_squares(num), square_of_sum(num)) - min(sum_of_squares(num), square_of_sum(num))
print(ans)