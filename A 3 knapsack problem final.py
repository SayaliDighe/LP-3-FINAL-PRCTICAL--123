class KnapsackPackage(object):
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.cost = value / weight

    def __lt__(self, other):
        return self.cost < other.cost

class FractionalKnapsack(object):
    def knapsackGreProc(self, W, V, M, n):
        packs = []   
        for i in range(n):
            packs.append(KnapsackPackage(W[i], V[i]))
            
        packs.sort(reverse=True)

        remain = M 
        result = 0 
        i = 0
        
        while remain > 0 and i < n:
            if packs[i].weight <= remain:  
                remain -= packs[i].weight
                result += packs[i].value
                print(f"Pack {i} - Weight {packs[i].weight} - Value {packs[i].value}")
            else:
                
                fraction = remain / packs[i].weight
                result += packs[i].value * fraction
                print(f"Pack {i} (fraction) - Weight {remain} - Value {packs[i].value * fraction}")
                remain = 0  
  
            i += 1

        print("Max Value:\t", result)

if __name__ == "__main__":
    W = []
    V = []
       
    num = int(input("Enter the number of weights or values required:\n"))
     
    for i in range(num):
        n = int(input(f"Enter weight {i + 1} : "))
        W.append(n)

    print("\n")
      
    for i in range(num):
        n = int(input(f"Enter value {i + 1} : "))
        V.append(n)

    print("\n")
    
    M = int(input("Enter the cost: "))
    n = len(V)
    print("\n")
    proc = FractionalKnapsack()
    proc.knapsackGreProc(W, V, M, n)
