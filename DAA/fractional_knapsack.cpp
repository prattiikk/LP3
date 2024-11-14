#include <iostream>
#include <vector>
using namespace std;

// Bubble Sort to sort the items based on their profit/weight ratio in descending order
void bubbleSort(vector<int> &weights, vector<int> &profits, vector<double> &ratio, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = 0; j < n - i - 1; j++)
        {
            if (ratio[j] < ratio[j + 1])
            {
                // Swap ratios
                swap(ratio[j], ratio[j + 1]);
                // Swap corresponding weights
                swap(weights[j], weights[j + 1]);
                // Swap corresponding profits
                swap(profits[j], profits[j + 1]);
            }
        }
    }
}

int main()
{
    int n; // Number of items
    cout << "enter the number or items available : ";
    cin >> n;

    double knapsackCapacity; // Knapsack capacity

    // Input the capacity of the knapsack
    cout << "Enter the Knapsack Capacity: ";
    cin >> knapsackCapacity;

    vector<int> weights(n);  // Weights of items
    vector<int> profits(n);  // Profits of items
    vector<double> ratio(n); // Profit/Weight ratio


    // Input weights and profits of items
    for (int i = 0; i < n; i++)
    {
        cout << "Enter Profit of item " << i + 1 << ": ";
        cin >> profits[i];
        cout << "Enter Weight of item " << i + 1 << ": ";
        cin >> weights[i];
    }

    // Calculate profit/weight ratio for each item
    for (int i = 0; i < n; i++)
    {
        ratio[i] = static_cast<double>(profits[i]) / weights[i];
    }

    // Sort items based on profit/weight ratio in descending order
    bubbleSort(weights, profits, ratio, n);



    double totalProfit = 0.0;

    // Greedy approach to select items
    for (int i = 0; i < n; i++)
    {
        if (weights[i] <= knapsackCapacity)
        {
            // If item can fully fit in the remaining capacity
            totalProfit += profits[i];
            knapsackCapacity -= weights[i];
        }
        else
        {
            // Take the fraction of the item
            totalProfit += profits[i] * (knapsackCapacity / weights[i]);
            break; // Knapsack is full, no more items can fit
        }

        // If the knapsack is full, break the loop
        if (knapsackCapacity == 0)
        {
            break;
        }
    }

    // Output the maximum profit
    cout << "Maximum profit: " << totalProfit << endl;

    return 0;
}