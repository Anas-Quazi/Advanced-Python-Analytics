
#todo import module
import My_module

#? access attributes and methods
print(My_module.skills)
print(My_module.totalSkills())

#* from (module) import (attribute/method)
from My_module import skills
from My_module import totalSkills
print(totalSkills())

help(totalSkills)