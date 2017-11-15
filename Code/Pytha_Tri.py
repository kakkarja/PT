# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:40:37 2017

@author: karja
"""

from math import sqrt

# The best formula for GCD that can be found in wikipedia
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# Class that set the dict that represent the 
# range of pythagores that have integer values.
class Pytha_tri:
    def __init__(self,num1):
        self.num1 = num1
    def pair_em(self):
        
        # This taken from the book 
        # Learning Python from PACKT by (thanks to) Fabrizio Romano.
        legs = [(a,b,sqrt(a**2 + b**2)) for a in range(1,self.num1) for b in range(a,self.num1)]
        legs = [(a,b,int(c)) for a, b, c in legs if c.is_integer()]
        for m in range(1,int(self.num1**.5)+1):
            for n in range(1,m):
                
                # Alternate additional condition (and (m-n)%2 == 1:)
                if gcd(m,n) == 1: 
                    
                    # Eucledean formula for finding triple pythagorean
                    # (a,b,c) => a= m**2 - n**2, b = 2mn , c =m**2 + n**2
                    # Where (m,n) have GCD of 1
                    if m > n:
                        a = m**2 - n**2
                    else:
                        a = n**2 - m**2
                    b = 2*m*n
                    c = m**2 + n**2
                    legs.append((a,b,c))
        
        # I made this class to compliment the pythagores triple that
        # thought in the book.
        check = [((a**2+b**2)==c**2) for a, b, c in legs ]
        check = {a:b for a,b in zip(legs,check)}
        return check
        print(check)
        
# Globals that can be called within the functions.        
pairs = {}
pytha_num = None

# Function that give max values to Pytha_tri and assign globals variables.
def call_p(nums):
    global pairs,pytha_num
    pairs = Pytha_tri(nums).pair_em()
    pytha_num = Pytha_tri(nums)
    
import unicodedata as uni

# Function that will test your knowledge about Pythagores formulas in fun way 
# because the result will true if integer and will be false if float.
def gpyt():
    
    # Translating and printing the a² + b² = c²
    sup2 = str.maketrans('2',uni.normalize('NFC',u'\u00B2'))
    print('Pythagorean triple with total records of', len(pairs),'\nFormula of a2 + b2 = c2'.translate(sup2))
    
    # The try out of Phytagorean Triple
    while True:
        try:
            triple = tuple([int(b) for b in input('input 3 numbers e.g. 1 2 3 : ').split()])
        except:
            print('Please input number e.g 1 2 3')
            continue
        else:
            try:
                a, b, c = triple
            except:
                print('Please input number e.g 1 2 3')
                continue
            else:
                
                # Checking the answer if is True or False
                print (triple, triple[0]**2 + triple[1]**2, '=', triple[2]**2, pairs.get(triple,False))
                
                # If is true then the record is deleted
                if pairs.get(triple,False) == True:
                    pairs.pop(triple,True)
                    break
                else:
                    break
                
# The game begin with How many records that can be generated
# and try to guess them all out.    
def run_gpyt():
   
    while True:
        
        # Create records
        in_num = input('Create list of Pythagorean Triple, give numbers' + 
                  '\ngreater than 5 and less then 1000: ')
    
        try:
            int(in_num)
        except:
            print('Please Key integer numbers')
            continue
        else:
            if int(in_num) < 5:
                print('Numbers are too small')
                continue
            elif int(in_num) > 1000:
                print('Numbers are too big')
                continue
            else:
                call_p(int(in_num))
                break
    
    # Start playing
    gpyt()
    while True:        
        try:
            
            # To continue or end
            quest = str(input('Continue? [Y]es or Enter: ').upper())
        except:
            print('Please key in "Y" to continue or Enter to end!')
            continue
        else:
            if quest == 'Y':
                
                # Checking the records
                if len(pairs) > 0:
                    gpyt()
                    continue
                else:
                    
                    # If record is 0 then game is finished and end.
                    print('Congratulation, you have finished the game.')
                    input()
                    break
            else:
                if len(pairs) == 0:
                    print('Congratulation, you have finished the game.')
                    input()
                    break
                else:
                    break
    
# Self-started
run_gpyt()  