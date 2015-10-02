__author__ = 'student'
from random import *
output = open('privet.txt', 'w')
for i in range(0,999999):
    output.write(randint(0,100))
output.close()

