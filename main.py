from lmfit import minimize, Parameters
import numpy as np
import random


def format_float(num):
    return np.format_float_positional(num, trim='-')

def Rosenbrock_Numpy_function(parameters):
    return np.array([10 * (parameters['yLabel'] - parameters['xLabel'] * parameters['xLabel']), (1 - parameters['xLabel'])])

def Rosenbrock_function(x, y):
    return (1 - x) * (1 - x) + 100 * (y - (x * x)) * (y - (x * x))

def append_new_steps(parameters, iter, resid):
    xArray.append(parameters['xLabel'].value)
    yArray.append(parameters['yLabel'].value)

xArray = []
yArray = []

random.seed()
maximum = 100

value_1 = random.random() * maximum
value_2 = random.random() * maximum

print(f"\nRandom x coordinate: {value_1}")
print(f"Random y coordinate: {value_2}")

initial_points = []
initial_points.append(value_1)
initial_points.append(value_2)

print(f"Therefore we begin at P = {initial_points}")


guessing_points = Parameters()
xArray.append(initial_points[0])
yArray.append(initial_points[1])
guessing_points.add('xLabel', value = initial_points[0])
guessing_points.add('yLabel', value = initial_points[1])
initial_points = minimize(Rosenbrock_Numpy_function, guessing_points, iter_cb=append_new_steps)

output_value_of_x = xArray.pop()
output_value_of_y = yArray.pop()


print(f"\nEstimated coordinates = [{output_value_of_x}, {output_value_of_y}]\n")

print("Consecutive steps: ")
for x in range(len(yArray)):
    print(f"-> step={x}, x={xArray[x]:.4f}, y={yArray[x]:.4f}, f(x, y)={format_float(Rosenbrock_function(xArray[x], yArray[x]))}") 


outputAnswer = Rosenbrock_function(output_value_of_x, output_value_of_y)
print(f"\nEstimated minimum of the Rosenbrock function is in ({output_value_of_x}, {output_value_of_y}) and is equal to {outputAnswer:.4f}")