#approach1:
import a
import b
obj=a.Animal()    ##modulename.class name
obj.display()
obj1=b.Bird()     #modulename.class name
obj1.display()

#approach2:
from a import Animal
from b import Bird
obj=Animal()
obj.display()
obj1=Bird()
obj1.display()