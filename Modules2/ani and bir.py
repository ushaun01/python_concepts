#approach1:
import Animal
import Bird
Animal.fly()
Animal.colour()
Bird.fly()
Bird.colour()

#approach2:
from Animal import *
fly()
colour()
from Bird import *
fly()
colour()