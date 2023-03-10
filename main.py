from lmfit import minimize, Parameters
from more_itertools import consecutive_groups
import numpy as np
from array import array
import random

xArray = []
yArray = []

def format_float(num):
    return np.format_float_positional(num, trim='-')

random.seed()
maximum = 100

value_1 = random.random() * maximum
value_2 = random.random() * maximum

print(f"\nRandom x coordinate: {value_1}")
print(f"Random y coordinate: {value_2}")

initialMinimumPointGuess = []
initialMinimumPointGuess.append(value_1)
initialMinimumPointGuess.append(value_2)

print(f"Therefore we begin at P = {initialMinimumPointGuess}")


def RosenbrockNumpyFunction(parameters):
    return np.array([10 * (parameters['yLabel'] - parameters['xLabel'] * parameters['xLabel']), (1 - parameters['xLabel'])])


def appendingNewStepsValues(parameters, iter, resid):
    xArray.append(parameters['xLabel'].value)
    yArray.append(parameters['yLabel'].value)


guessingPoints = Parameters()
xArray.append(initialMinimumPointGuess[0])
yArray.append(initialMinimumPointGuess[1])
guessingPoints.add('xLabel', value = initialMinimumPointGuess[0])
guessingPoints.add('yLabel', value = initialMinimumPointGuess[1])
initialMinimumPointGuess = minimize(RosenbrockNumpyFunction, guessingPoints, iter_cb=appendingNewStepsValues)

output_value_of_x = xArray.pop()
output_value_of_y = yArray.pop()


print(f"\nEstimated coordinates = [{output_value_of_x}, {output_value_of_y}]\n")

def singleInputsRosenbrockFunction(x, y):
    return (1 - x) * (1 - x) + 100 * (y - (x * x)) * (y - (x * x))

print("Consecutive steps: ")
for x in range(len(yArray)):
    print(f"-> step={x}, x={xArray[x]:.4f}, y={yArray[x]:.4f}, f(x, y)={format_float(singleInputsRosenbrockFunction(xArray[x], yArray[x]))}") 


#for x in range(len(yArray)):
 #   print(format_float(singleInputsRosenbrockFunction(xArray[x], yArray[x])))

outputAnswer = singleInputsRosenbrockFunction(output_value_of_x, output_value_of_y)
print(f"\nEstimated minimum of the Rosenbrock function is in ({output_value_of_x}, {output_value_of_y}) and is equal to {outputAnswer:.4f}")