#include <iostream>
using namespace std;

// Global variable to count the steps
int stepCount = 0;

// Recursive function to calculate Fibonacci
int fibonacciRecursive(int n) {
    stepCount++; // Increment step count for each function call
    
    // Base cases
    if (n <= 1)
        return n;

    // Recursive calls
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Function to calculate Fibonacci using iteration
int fibonacciIterative(int n) {
    stepCount = 0;  // Reset step count for each calculation

    if (n <= 1) {
        return n;  // Base case
    }

    int first = 0, second = 1, fib;
    
    // Iterative calculation of Fibonacci
    for (int i = 2; i <= n; i++) {
        stepCount++;  // Count each iteration step
        fib = first + second;
        first = second;
        second = fib;
    }

    return fib;  // Return the nth Fibonacci number
}

int main() {
    int n, choice;
    
    cout << "Enter the position of Fibonacci number: ";
    cin >> n;

    cout << "Choose method to calculate Fibonacci number:\n";
    cout << "1. Recursive\n";
    cout << "2. Iterative\n";
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;

    int result;
    
    // Perform calculation based on user choice
    if (choice == 1) {
        result = fibonacciRecursive(n);
        cout << "Fibonacci number at position " << n << " (recursive) is: " << result << endl;
    } else if (choice == 2) {
        result = fibonacciIterative(n);
        cout << "Fibonacci number at position " << n << " (iterative) is: " << result << endl;
    } else {
        cout << "Invalid choice!" << endl;
        return 1;
    }

    cout << "Number of steps taken: " << stepCount << endl;

    return 0;
}