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

########################
# Normal Distributions #
#######################
def normDist(SD, avg, L):
    if SD == 0:
        return "Standard Deviation of 0"
    
    lengths = []
    for j in L:
        lengths.append(len(j))
    
    points = []
    for i in  lengths:
        points.append((1/(SD*math.sqrt(2*math.pi))*(math.e)**(((-1/2)*(i-avg)/SD)**2)))

    return points

# SHOULD RETURN 0
L = ['a', 'z', 'p']
print("STANDARD DEVIATION OF LENGTH:  ",stdDevOfLengths(L))
print("COEFFICIENT OF VARIATION:  ", coefVar(*(stdDevOfLengths(L))), '\n')  
print("NORMAL DISTRIBUTION POINTS:  ", normDist(*(stdDevOfLengths(L)),L), '\n')


# SHOULD RETURN 1.8708    
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print("STANDARD DEVIATION OF LENGTH:  ",stdDevOfLengths(L))
print("COEFFICIENT OF VARIATION:  ", coefVar(*(stdDevOfLengths(L))), '\n')  
print("NORMAL DISTRIBUTION POINTS:  ", normDist(*(stdDevOfLengths(L)),L), '\n')

L = ['tttttttttt', 'tttt', 'tttttttttttt', 'ttttttttttttttt', 'tttttttttttttttttttt', 'ttttt']
print("STANDARD DEVIATION OF LENGTH:  ", stdDevOfLengths(L))
print("COEFFICIENT OF VARIATION:  ", coefVar(*(stdDevOfLengths(L))))
print("NORMAL DISTRIBUTION POINTS:  ", normDist(*(stdDevOfLengths(L)),L), '\n')
