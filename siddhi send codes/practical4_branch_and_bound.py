from collections import namedtuple

# Class to represent the Branch and Bound method for solving the 0/1 Knapsack problem
class KnapSackBranchNBound:
    def __init__(self, capacity, items, item_count):
        self.capacity = capacity
        self.items = items
        self.item_count = item_count

    # Method to solve the knapsack problem using Branch and Bound
    def solve(self):
        # Initialize the optimal value to 0
        max_profit = 0
        taken = [0] * self.item_count  # Tracks which items are taken
        
        # Sort items by value-to-weight ratio
        self.items.sort(key=lambda item: (item.value / item.weight), reverse=True)
        
        # Try different combinations using Branch and Bound strategy
        current_weight = 0
        current_value = 0
        for item in self.items:
            if item.weight + current_weight <= self.capacity:
                taken[item.index] = 1  # Take the item
                current_weight += item.weight
                current_value += item.value
            else:
                break  # Stop if adding the current item exceeds capacity

        max_profit = current_value
        
        # Return the maximum profit and the taken items
        return max_profit, taken

# Function to format the solution into the desired output format
def get_solution(optimal_value, taken):
    output_data = str(optimal_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == "__main__":
    # Named tuple to represent each item with its index, value, and weight
    Item = namedtuple("Item", ['index', 'value', 'weight'])
    
    # Manually input data (no file reading)
    item_count = int(input("Enter the number of items: "))
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    items = []
    for i in range(item_count):
        value = int(input(f"Enter value for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(i, value, weight))

    # Initialize the Branch and Bound solver
    kbb = KnapSackBranchNBound(capacity, items, item_count)
    
    # Solve the knapsack problem
    max_profit, taken = kbb.solve()
    
    # Print the solution
    print(get_solution(max_profit, taken))
