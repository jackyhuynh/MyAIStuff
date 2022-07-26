#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:20:25 2021

@author: eshasharma
"""#
# import csv and random libraries

import csv
import pandas as pd
import random


# for random example 
from datetime import datetime

          
# Introductin to csv library and dict reader       
with open('homes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        #for row in reader:
           #print(row)
           #print(row['Acres'])
          

#Introduction to dataframes and csv reader    
df = pd.read_csv('homes.csv')
#for column in df:
    #print(column)
    #print(df[column])




# Introduction to random library and seed  
from random import seed
from random import random
from random import sample
from random import choices

# seed random number generator - this will be used to generate the random 
# numbers 
seed(1)
# generate some random numbers
print(random(), random(), random())

# reset the seed
seed(2)
# generate some random numbers
print(random(), random(), random()) 
# generate some random numbers based on current date    
seed(datetime.now())
# Generate 10 random numbers 
print(random(), random(), random())           
s = sample(range(5), k=1)
print(s)


population = [1, 2, 3, 4, 5, 6] #bandit arms
probabilities = [.1, .05, .05, .2, .4, .2] #probabilites
print(choices(population, probabilities))




































