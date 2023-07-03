# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:40:06 2023

@author: s1453918
"""

import numpy as np
import pandas as pd
import itertools as itr

CSV = ""

def calc_series_spring_const(*args): 

    try:
        ks_ = args[0].split(" ")
        ks = []
        for i in ks_:
            if i != "":
                ks.append(float(i))
        ks = np.array(ks)    
        k = (sum(1/ks))**-1
        result = "{:.4f}".format(k)  
    
    except ValueError:
        result = "Something went very wrong!"
        
    return result


def calc_parallel_spring_const(*args):     
    
    try:
        ks_ = args[0].split(" ")
        ks = []
        for i in ks_:
            if i != "":
                ks.append(float(i))
        ks = np.array(ks)    
        k = sum(ks) 
        result = "{:.4f}".format(k)  
    
    except ValueError:
        result = "Something went very wrong!"   

    return result


def find_spring_combinations_series(target, number_of_springs):

    try:

        target = float(target)
        number_of_springs = int(number_of_springs)
        error_band = 0.05

        if number_of_springs <= 2:
            spring_const_range = np.arange(target/10, target*10, target/10)
        else:
            spring_const_range = np.arange(target/5, target*5, target/5)

        combinations = list(itr.combinations(spring_const_range, number_of_springs))

        possible_combinations = []
        headers = []
        for i in range(number_of_springs):
            possible_combinations.append("{:.3f}".format(target*number_of_springs)) 
            headers.append("k%s" % (i+1))
        possible_combinations = [str(headers).replace("'","").replace("[","").replace("]","").replace(",",""), str(possible_combinations).replace("[","").replace("]","").replace(",","").replace("'","")]  

        for combination in combinations:

            string_combination = []
            for element in combination:
                string_combination.append("{:.3f}".format(element))
            string_combination = str(string_combination).replace("[","").replace("]","").replace(",","").replace("'","") 
            
            kt = float(calc_series_spring_const(string_combination))
            
            if ((kt <= (target*(1+error_band))) and (kt >= (target*(1-error_band)))):
                possible_combinations.append(string_combination)

        data = np.empty(shape=(len(possible_combinations), number_of_springs), dtype='<U11')
        for i in range(len(possible_combinations)):
            for j in range(number_of_springs):
                    data[i,j] = possible_combinations[i].split(" ")[j]
        
        result = pd.DataFrame(data[1:,:], columns=data[0,:])

        global CSV
        CSV = result
        
        headers = list(result.columns)
        data = result.values.tolist()

        result = [headers, data]


    except ValueError:
        result = "Something went very wrong!"   

    return result

def save_csv():

    if isinstance(CSV, pd.DataFrame):
        CSV.to_csv('saved_results.csv')
    else:
        pass

    return



# Test
# print(find_spring_combinations_series(0.02, 4))