# Estimating the minimum of Rosenbrock function using Levenberg-Marquardt method in Python
## 1. Introduction
The Rosenbrock function, also referred to as the Valley or Banana function, is a popular test problem for gradient-based optimization algorithms.

<div align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Rosenbrock_function.svg/720px-Rosenbrock_function.svg.png" style="width: 520px">
</div>

$$f(x,~y) ~ = ~ (1 ~ - ~ x)^2 ~ + ~ 100(y ~ - ~ x^2)^2$$

## 2. Levenberg-Marquardt method
To minimize a a multi-variable function you can use the Levenberg-Marquardt method which is used to solve non-linear least squares problems and is default in the minimize() function from lmfit library. The Levenberg–Marquardt algorithm (LMA) interpolates between the Gauss–Newton algorithm and the method of gradient descent. The LMA is more robust than the GNA, which means that in many cases it finds a solution even if it starts very far off the final minimum. 


## 3. Used technologies
- Python
- NumPy
- lmfit

## 4. How to use
You need to install NumPy, lmfit, and obviously Python itself.

```pip install numpy```

```pip install lmfit```

Then in the proper directory use:
```python main.py```
