#approach1:
import sys

from Package2.module1 import display

sys.path.append("D:/Pycharm/Python/Package2")
sys.path.append("D:/Pycharm/Python/Package2/Package3")
import module1
import module2
module1.display()
module2.show()

#approach2:
import sys
sys.path.append("D:/Pycharm/Python/Package2")
sys.path.append("D:/Pycharm/Python/Package2/Package3")
from module1 import *
from module2 import *
display()
show()