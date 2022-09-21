


import math as m
from operator import contains
from random import randint

x = 10

# Write a loop to go through and count the sum of the odd numbers up to n


def odd_sum(n):
    sum = 0
    count = 1
    iterator = 0
    while iterator < n:
        sum += count
        count += 2
        iterator += 1
    print(sum)

# && -> and, || -> or, ! -> not

# Write a function to find the factorial of n (non-recursive)


def fac(n):
    if n == 1:
        return 1

    return n * fac(n-1)


def factorial(n):
    ans = 1

    for i in range(n, 0, -1):
        # Start, Stop, Step -> for(int i = start; i < stop; i++)
        # default start is 0, default step is 1
        ans *= i

    return ans


for i in range(10):
    print(i)
    if i == 5:
        break


# GCD(m, n): m > n. Algorithm is as follows:
# while n != 0
# temp = m
# m = n
# n = temp % n
# return m
def GCD(m, n):
    while(n != 0):
        print(m, n, m % n)
        temp = m
        m = n
        n = temp % n

    return m


def sum_to_n(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


def dice():
    return randint(1, 6)

# Write a function to keep track of the result of the sum of 2 dice rolls n times, return the list that stores the information
# Ex: [1, 3, 5, 7, 9, 13, 7, 4, 3, 2, 1]


def diceCounter(n):
    results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(n):
        results[dice()+dice()-2] += 1

    return results


def dice_counter(n):
    results = {}

    for i in range(2, 13):
        results[i] = 0
    for i in range(n):
        results[dice() + dice()] += 1

    return results

def main():
    odd_sum(5)