print(2 % -4)
print(3 % -9)

x =  -1
x = float(x)
y = 3*(x**3) - 2*(x**2) + 3*x -1
print("y =", y)

a = 6
b = 3
a /= 2 * b
print(a)


# anything = input("Tell me anything...")
# print("Hmm...", anything, "... Really?")

print('James' * 4)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

########################################################

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# hours_taken = dura // 60 # Write your code here.
# minutes_additional = dura % 60
# extra_mins = (mins + minutes_additional)
# end_mins = extra_mins % 60
# end_hour = (hour + hours_taken + extra_mins // 60) % 24


# print('end time: ' + str(end_hour) + ':' + str(end_mins))

print(3 % 4)
print(1 // 2 * 3)

print("\n*********\n")

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)