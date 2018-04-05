# Quadratic
import math

def quadratic(a, b, c):
	if(a == 0):
		return -c/b
	if((b*b - 4 * a * c) < 0):
		return [ complex(-b/2*a, +math.sqrt(abs(b*b - 4 * a * c))/(2*a)), complex(-b/2*a, +math.sqrt(abs(b*b - 4 * a * c))/(2*a)) ]
	return [(-b + math.sqrt(b*b - 4 * a * c))/(2*a), (-b - math.sqrt(b*b - 4 * a * c))/(2*a) ]



print(quadratic(2,-1,-1))

print(quadratic(1,4,4))

print(quadratic(3,11,0))

print(quadratic(4,0,8))

print(quadratic(0,4,4))

# [1.0, -0.5]
# [-2.0, -2.0]
# [0.0, -3.6666666666666665]
# [1.4142135623730951j, 1.4142135623730951j]
# -1.0