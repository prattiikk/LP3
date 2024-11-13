import numpy as np
import matplotlib.pyplot as plt

# Define the function to minimize: f(x) = (x + 3)^2
def f(x):
    return (x + 3) ** 2

# Define the derivative of the function (used to find the gradient): f'(x) = 2 * (x + 3)
def df(x):
    return 2 * (x + 3)

# Initial starting point
x = 2  

# Learning rate (controls the step size in each iteration)
learning_rate = 0.1

# Number of iterations (controls how many steps we take)
iterations = 50

# Lists to store x and y values for plotting the gradient descent path
x_values = []
y_values = []

# Perform gradient descent
for i in range(iterations):
    x_values.append(x)         # Store current x value for plotting
    y_values.append(f(x))      # Store current y = f(x) value for plotting
    gradient = df(x)           # Calculate the gradient (slope) at the current x
    x = x - learning_rate * gradient  # Update x to move towards the minimum

# Print the result of gradient descent
print(f"Local minimum found at x = {x}, with f(x) = {f(x)}")

# Prepare data for plotting the function curve
x_range = np.linspace(-6, 2, 100)  # x values from -6 to 2
y_range = f(x_range)               # Calculate corresponding y values using f(x)

# Plot the function and gradient descent path
plt.figure(figsize=(10, 10))

# Plot the function curve y = (x + 3)^2
plt.plot(x_range, y_range, label='y = (x + 3)²', color='blue')

# Plot each step in the gradient descent path as red dots
plt.scatter(x_values, y_values, color='red', label='Iterations', zorder=5)

# Adding labels and lines for visualization
plt.title('Gradient Descent Steps')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='red', lw=0.5, ls='--')        # Red dashed line at y = 0
plt.axvline(-3, color='green', lw=1, ls='--', label='Minimum at x = -3')  # Green line at x = -3 (minimum)

# Show the plot
plt.legend()
plt.show()