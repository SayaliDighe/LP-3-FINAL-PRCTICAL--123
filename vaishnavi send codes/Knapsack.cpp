#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Structure to store information about items
struct Item {
    int weight;
    int profit;

    // Constructor for easier initialization
    Item(int w, int p) : weight(w), profit(p) {}
};

// Function to solve the 0-1 Knapsack problem using dynamic programming
int zeroOneKnapsack(int W, vector<Item>& items) {
    int n = items.size();
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    // Build the dp array
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (items[i - 1].weight <= w) {
                // Include the item or exclude it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].profit);
            } else {
                // Cannot include the item
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // The maximum profit will be in the last cell of the dp array
    return dp[n][W];
}

int main() {
    int n, W;
    cout << "Enter the number of items: ";
    cin >> n;
    cout << "Enter the capacity of the knapsack: ";
    cin >> W;

    vector<Item> items;
    for (int i = 0; i < n; i++) {
        int weight, profit;
        cout << "Enter weight and profit for item " << i + 1 << ": ";
        cin >> weight >> profit;
        items.push_back(Item(weight, profit));
    }

    int maxProfit = zeroOneKnapsack(W, items);
    cout << "Maximum profit in the knapsack = " << maxProfit << endl;

    return 0;
}