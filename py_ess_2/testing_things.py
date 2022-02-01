import math
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print('testing the things')

math_dir = dir(math)

# for d in math_dir:
#     print(d)

# print(math.ceil(45.000000001))
# print(math.floor(46.99999999999))

print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor()) # name of CPU
print(system())
print(version())
print(python_implementation())
print(python_version_tuple())