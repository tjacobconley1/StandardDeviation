# -*- coding: utf-8 -*-
"""
Standard Deviation 
(to use as reference)
Author: Tyler Conley
Date: 11-26-2021
"""

import math
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

######################
# STANDARD DEVIATION #
######################
def stdDevOfLengths(L):
    """
    L: a list of strings
    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    lengths = []
    summation = 0
    N = len(L)
    
    # N = length of the list 
    if N == 0:
        return float('NaN')
    
    # creates a list containing the lengths 
    # of each string in the list L
    for i in L:
        lengths.append(len(i))
    
    # u = the sum of all list elements 
    #      divided by the number of elements
    u = sum(lengths)
    u = u/N
    
    # t = each individual element to be
    #      iterated over 
    for t in lengths:
        summation += (t-u)**2
    
    # finally take the square root of the 
    # summation divided by the length of the list 
    return (math.sqrt(summation/N), u)
    

############################
# Coefficient of Variation #
############################
def coefVar(SD, avg):
    return SD/avg    


    
# SHOULD RETURN 0
L = ['a', 'z', 'p']
print(stdDevOfLengths(L))
print("coefficient of variation", coefVar(*(stdDevOfLengths(L))), '\n')  

# SHOULD RETURN 1.8708    
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
print("coefficient of variation", coefVar(*(stdDevOfLengths(L))))
