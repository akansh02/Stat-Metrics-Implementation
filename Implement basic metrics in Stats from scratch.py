#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement : 
# 
# #### - Given a list of numbers, please implement  Statistical metrics from scratch without using NumPy/SciPy/other libraries.
# #### - Once you compute these metrics, compare them against the values obtained using standard libraries like NumPy/SciPy to see that your code is correct.

# In[1]:


import numpy as np
import math
from scipy import stats

lst = [1,2,4,3,6,5,7,21,22,8,9,3]


print("********************  1. MEAN  ***********************************")

# Mean
def Mean(lst):
    n = len(lst)
    mean = sum(lst)/n
    return mean

print("MY MEAN",Mean(lst))

# Cross verifying using Numpy mean function 
check_mean = np.mean(lst)

print("NUMPY MEAN",check_mean)

print("*********************** 2. MEDIAN ************************************")

# Median

def Median(lst):
    ordered_lst = sorted(lst)
    n = len(lst)

    if n%2 == 0: #if even
    
        median_1 = ordered_lst [(n//2)-1]
        median_2 = ordered_lst [(n//2)]
        median = (median_1 + median_2)/2
        return median
    else: #if odd
        median = ordered_lst [(n//2)]
        return median

print("MY MEDIAN",Median(lst))
    
# Cross verifying using numpy median function
ordered_lst = sorted(lst)
print("NUMPY MEDIAN",np.median(ordered_lst))


print("*********************** 3. VARIANCE ************************************")

# Variance
def Variance(lst):
    var= []
    n = len(lst)
    for i in lst:
        var.append((i-Mean(lst))**2)
    variance = sum(var)/n
    return variance


print("MY VARIANCE",Variance(lst))


# Cross Verifying
print("NUMPY VARIANCE",np.var(lst))


print("********************* 4. STD-DEV **************************************")

# Std-Dev
def Std_Dev(lst):
    return math.sqrt(Variance(lst))

print("My Std-dev", Std_Dev(lst))

#Cross verifying
print("NUMPY Std-dev",np.std(lst))


print("*********************  5. IQR   **************************************")

# IQR
def Percentile(value):
    n = len(lst)
    ordered_lst = sorted(lst)
    Percentile_term = round(((n-1)/(100/value)),3)
    
    int_part = int(Percentile_term//1)
    decimal_part = Percentile_term % 1
    
    Percentile_value =  ordered_lst[int_part] + decimal_part * (ordered_lst[int_part+1] - ordered_lst[int_part])
    return Percentile_value

def IQR(lst):
    Q3 = Percentile(75)
    Q1 = Percentile(25)
    IQR = Q3 - Q1
    return IQR

print("MY IQR", IQR(lst))

#using stats}
Q3_75 , Q1_25 = np.percentile(lst, [75 , 25])
IQR = Q3_75 - Q1_25
  
print("STATS IQR",IQR)


print("***************** 6. 90th PERCENTILE ***********************")

# 90th Percentile

print("MY PERCENTILE",Percentile(90))

print("NUMPY PERCENTILE",np.percentile(lst, 90))


print("***************** 7. 99th PERCENTILE ***********************")

# 99th Percentile

print("MY PERCENTILE",Percentile(99))

print("NUMPY PERCENTILE",np.percentile(lst, 99))




# Median-Absolute Deviation

print("***************** 9. Median-Absolute Deviation ***********************")

def MedianAbsDeviation(lst):
        abs_dev =[]
        for values in lst:
            abs_dev.append(abs(values - Median(lst)))
        MAD = Median(abs_dev)
        return MAD
     
print("MY MAD:", MedianAbsDeviation(lst))

print("Numpy MAD:" ,np.median(np.absolute(lst - np.median(lst))))



# In[ ]:




