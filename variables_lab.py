force = float(input("Enter the force in newtons: "))
distance = float(input("Enter the distance in meters: "))
work = force * distance
print("work:", work)

# 120 force * 2 distance = 240 work
# I assume the type is an integer

print(type(work))

time = 12
power = work / time
print("power:", power)
print(type(power))

fun = work % power
print("fun", fun)
print(type(fun))
