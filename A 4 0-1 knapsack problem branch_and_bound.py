from collections import namedtuple


class KnapSackBranchNBound:
    def __init__(self, capacity, items, item_count):
        self.capacity = capacity
        self.items = items
        self.item_count = item_count

    
    def solve(self):
        
        max_profit = 0
        taken = [0] * self.item_count 
        
        self.items.sort(key=lambda item: (item.value / item.weight), reverse=True)
        
        current_weight = 0
        current_value = 0
        for item in self.items:
            if item.weight + current_weight <= self.capacity:
                taken[item.index] = 1  
                current_weight += item.weight
                current_value += item.value
            else:
                break  

        max_profit = current_value
         
        return max_profit, taken


def get_solution(optimal_value, taken):
    output_data = str(optimal_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

if __name__ == "__main__":
    
    Item = namedtuple("Item", ['index', 'value', 'weight'])
    
    
    item_count = int(input("Enter the number of items: "))
    capacity = int(input("Enter the capacity of the knapsack: "))
    
    items = []
    for i in range(item_count):
        value = int(input(f"Enter value for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(i, value, weight))

    
    kbb = KnapSackBranchNBound(capacity, items, item_count)
    
    max_profit, taken = kbb.solve()
     
    print(get_solution(max_profit, taken))
