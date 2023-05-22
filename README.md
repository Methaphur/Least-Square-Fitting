# Least Square Fitting 

This program implements a least square fitting algorithm to find the best-fit line that minimizes the sum of squared differences between the observed data points and the predicted values. The program takes a set of data points as input and calculates the values of `a` and `b` (intercept and slope) of the best fit line.

## How it works

The program follows the least square fitting method using the following equations:

$\sum y = na + b\sum x \quad \text{(1)}$

$\sum xy = a\sum x + b\sum x^2 \quad \text{(2)}$

where $\\sum x\$ represents the sum of the x-values of the data points, $\\sum y\$ represents the sum of the y-values, and $\sum xy\$ represents the sum of the products of $x$ and $y$.
and $n$ is the number of data points

By solving these equations simultaneously, the program determines the values of `a` and `b`, which represent the intercept and slope of the best-fit line or curve.

### Error Analysis

Errors in Least Square fit are given by

$\sigma_y = \sqrt{\frac{1}{N-2} \dot \sum_{i=1}^{N} (y_i - A - Bx_i)^2}$

$\Delta = N \sum{x^2} - (\sum{x})^2$ 

$\sigma_B = \sigma_y \cdot \sqrt{\frac{N}{\Delta}}$

$\sigma_A = \sigma_y \cdot \sqrt{\frac{\sum{x^2}}{\Delta}}$

## Usage

To use the program, follow these steps:

1. Provide the input data points in the code itself.
2. Run the program.
3. The program will calculate the values of `a` and `b`.
4. The output will be displayed, showing the equation of the best-fit line.

## Dependencies

The program has the following dependencies:

- Libraries: numpy , tabulate , matplotlib

Make sure to install the necessary dependencies before running the program.

## Example

Here's an example of using the program:

Input data points:
```
x_data = [3.80,8.26,15.31,19.31,21.39,26.52,36.27,40.79,43.01,62.79]
y_data = [0.109,0.231,0.409,0.472,0.566,0.700,0.941,1.315,1.441,2.073]
```

Output:
```
+-------+-------+-----------+-----------+
|    Xi |    Yi |     Xi*Yi |       Xi² |
+=======+=======+===========+===========+
|  3.8  | 0.109 |   14.44   |   0.4142  |
|  8.26 | 0.231 |   68.2276 |   1.90806 |
| 15.31 | 0.409 |  234.396  |   6.26179 |
| 19.31 | 0.472 |  372.876  |   9.11432 |
| 21.39 | 0.566 |  457.532  |  12.1067  |
| 26.52 | 0.7   |  703.31   |  18.564   |
| 36.27 | 0.941 | 1315.51   |  34.1301  |
| 40.79 | 1.315 | 1663.82   |  53.6388  |
| 43.01 | 1.441 | 1849.86   |  61.9774  |
| 62.79 | 2.073 | 3942.58   | 130.164   |
+-------+-------+-----------+-----------+

The Equation of the best fit is y = 0.03391397259201393*x + -0.11524316956542634

∑(x)  = 277.45
∑(y)  = 8.257
∑(xy) = 328.27911
∑(x²) = 10622.5635

Slope = 0.03391397259201393
Intercept = -0.11524316956542634

Error in Slope = 0.0017601988467113167
Error in Intercept = 0.057368883795324725

σy = 0.0951926415426897
∆ = 29247.13250000002
```
