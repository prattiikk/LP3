#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Memoization helper function to solve the 0/1 Knapsack problem
int knapsack(int W, const vector<int>& weights, const vector<int>& values, int n, vector<vector<int>>& dp) {
    // Base case: no items left or capacity is 0
    if (n == 0 || W == 0) {
        return 0;
    }

    // Check if the result is already computed
    if (dp[n][W] != -1) {
        return dp[n][W];
    }

    // If the weight of the nth item is greater than the current capacity, exclude it
    if (weights[n - 1] > W) {
        return dp[n][W] = knapsack(W, weights, values, n - 1, dp);
    } else {
        // Include the nth item or exclude it
        return dp[n][W] = max(
            values[n - 1] + knapsack(W - weights[n - 1], weights, values, n - 1, dp), // Include item
            knapsack(W, weights, values, n - 1, dp) // Exclude item
        );
    }
}

int main() {
    int n, W;
    cout << "Enter the number of items: ";
    cin >> n;
    cout << "Enter the capacity of knapsack: ";
    cin >> W;

    vector<int> values(n), weights(n);
    cout << "Enter value and weight for each item:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "Item " << (i + 1) << " - Value: ";
        cin >> values[i];
        cout << "Item " << (i + 1) << " - Weight: ";
        cin >> weights[i];
    }

    // Create a DP table initialized to -1 (indicating that no subproblem has been solved yet)
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, -1));

    // Call the knapsack function with the memoization table
    int maxProfit = knapsack(W, weights, values, n, dp);

    cout << "Maximum value in Knapsack = " << maxProfit << endl;

    return 0;
}