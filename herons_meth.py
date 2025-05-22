#Babylonian method of calculating the square root of a non-perfect square
#The purpose of this is to eventually use it to calculate the square root in vhdl and I am
#testing out the numerical methods. 
#Babylonian Method/Heron's Formula for approximating the square root:
#EQN 1.      y = (1/2)[a + (x/a)]
#Where y is the square root of some value. For example y = sqrt(14) where x = 14 in  EQN1. (1/2)[a + (x/a)]
#The way this works is by doing a closest approximation and plugging in the error into the iterative equation EQN1.
# Ex:  let's find sqrt(14)
#        y = sqrt(14)
#Closest value is sqrt(16) = 4
#   y = (1/2)[4 + (x/4)]              a = 4 in EQN1 and x = 14
#   y1 = 3.75           where y1 is iteration 1
#   y2 = (1/2)[3.75 + (14/3.75)]  
#   y2 = 3.742
#   y3 = (1/2)[3.742 + (14/3.742)]    = 3.742      <--- Approximately 
#Real answer is sqrt(14) = 3.7416574...
import numpy as np

x = 14  #number we want to caluclate the square root of 

perfect_squares = np.array([1,4,9,16,25,36,49,64,81,100,121,144,169])    #array containing perfects square
difference_array = perfect_squares - x                                   #find the difference of each element in the array

for i in perfect_squares:
    if difference