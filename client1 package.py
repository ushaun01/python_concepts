#approach1
import sys
sys.path.append("D:/Pycharm/Python/Package1")

import module1
import module2
module1.display()
module2.show()

#approach2
from module1 import *
from module2 import *
display()
show()