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

// Comparison function to sort items by profit-to-weight ratio
bool compare(Item a, Item b) {
    double r1 = (double)a.profit / a.weight;
    double r2 = (double)b.profit / b.weight;
    return r1 > r2;
}

double fractionalKnapsack(int W, vector<Item>& items) {
    // Sort items by profit-to-weight ratio in descending order
    sort(items.begin(), items.end(), compare);

    double totalProfit = 0.0;  // Total profit from selected items
    int currentWeight = 0;     // Current weight in knapsack

    for (const auto& item : items) {
        if (currentWeight + item.weight <= W) {
            // If adding the whole item is possible
            currentWeight += item.weight;
            totalProfit += item.profit;
        } else {
            // Add fraction of the item if it doesn't fit entirely
            int remainingWeight = W - currentWeight;
            totalProfit += item.profit * ((double)remainingWeight / item.weight);
            break;  // Knapsack is now full
        }
    }

    return totalProfit;
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

    double maxProfit = fractionalKnapsack(W, items);
    cout << "Maximum profit in the knapsack = " << maxProfit << endl;

    return 0;
}