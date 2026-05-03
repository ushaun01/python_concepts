#approach1:
import Calculator
Calculator.add(10,20)         #module name.function name()
Calculator.mul(15,12)

#approach2: for specific functions
from Calculator import add
add(100,200)

#approach3: for all functions * is used
from Calculator import *
add(25,20)
mul(12,2)
