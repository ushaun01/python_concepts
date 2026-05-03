#approach1:
import sys
sys.path.append("D:/Pycharm/Python/Package4")
sys.path.append("D:/Pycharm/Python/Package5")
import emp
obj1=emp.Employee(104,50000,"usha")
obj1.display1()
import stu
obj2=stu.Student(105,76,"anaye")
obj2.displaystu()

#approach2:
import sys
sys.path.append("D:/Pycharm/Python/Package4")
sys.path.append("D:/Pycharm/Python/Package5")
from emp import *
obj1=Employee(104,50000,"usha")
obj1.display1()
from stu import *
obj2=Student(105,76,"anaye")
obj2.displaystu()