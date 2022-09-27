from cuber.actuator.actuator_realization import *


controller = Controller(runner='ray',scheduler='scheduler')
print(type(controller.manager.obj))
print(controller.manager.name)




