# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:06:19 2020

@author: Neel
"""

fruitList = []

# to add fruits to the list
def addFruit(x): 
    if isinstance(x, str):
        print('Fruit added to the list')
        fruitList.append(x.lower())
    else: 
        print("Can't add the input to the list as it is not a string")

# to get the frequency of fruit names
def countFrequency(my_list):   
    # Creating an empty dictionary  
    freq = {} 
    for items in my_list: 
        freq[items] = my_list.count(items) 
    return(freq)
      
    
# user input to add fruits     
while True:    
    f = input("Please enter a fruit name:\n")
    addFruit(f)
    c = input("Do you want to add another fruit (y/n):\n")
    
    if c.lower() != 'y':
        break

freqList = countFrequency(fruitList)

# user input to get k value to find fruit with k occurences      
while True:    
    k = input("Please enter a value of k:\n")
    
    op = []
    for key, value in freqList.items(): 
        if value == int(k):
            op.append(key)
    
    print
    if len(op)>0:
        print(op)
    else:
        print('No fruits with k occurences')

    c = input("Do you want to try another value of k (y/n):\n")
        
    if c.lower() != 'y':
        break
    
