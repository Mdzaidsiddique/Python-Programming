import my_module as mm

print(mm.owner)

from my_module import owner_details
print(owner_details["name"])


# built in modules: math, copy, time, plateform etc

import platform
print(dir(platform)) #List all the defined names belonging to the platform module:

import platform

x = platform.system()
print(x) #windows