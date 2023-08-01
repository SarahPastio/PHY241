#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:01:29 2022

@author: sarah
"""

from math import sqrt, factorial

def dropTime():
    """
    Problem-A: Another ball dropped from a tower
    
    A ball is dropped from a tower of height h with initial velocity zero. Write a program that asks
    the user to enter the height in meters of the tower and then calculates and prints the time the
    ball takes until it hits the ground, ignoring air resistance. Use your program to calculate the
    time for a ball dropped from a 100 m high tower.
    """
    
    h = float(input("Please enter the height of the tower in meters: "))
    t = float(sqrt(2*h/9.81))
    
    print("The ball takes",t,"seconds to hit the ground.")
    
    
def madelungCon(L):
    """
    Write a program to calculate and print the Madelung constant for sodium chloride. Use as
    large a value of L as you can, while still having your program run in reasonable time—say in a
    minute or less.
    """
    M = 0
    
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range (-L,L+1):
                if not i==j==k==0:
                    if (i+j+k) % 2 == 0:
                        evenodd = -1
                    else:
                        evenodd = 1
                        
                    M += evenodd * 1/sqrt(i**2 + j**2 + k**2)             
    print("M =", M)
    
 
# Binomial, Pascal, Probability
def binomial(n,k):
    if n>=k:
        if k >= 1:
            coefficient = int(factorial(n)/(factorial(k)*factorial(n-k)))
            return coefficient
        elif k == 0:
            return 1
        else:
            print("Please give a positive value of k.")
    
def pascal():
    for i in range(1,21):
        for j in range(i+1):
            print(binomial(i, j), end= " ")
        print('\n')
    
def probability():
    # probability that a coin will come up heads exactly 60/100 times
    p60 = binomial(100, 60)/2**100
    
    # probability that a coin will come up heads 60-100 times
    p60_100 = 0
    for i in range(60,101):
        p60_100 += binomial(100, i)/2**100
        
    print("The probability that the coin will come up heads exactly 60 times is",p60,".")
    print("The probability that the coin will come up heads more than 60 times is",p60_100,".")
        
