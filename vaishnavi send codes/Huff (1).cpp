#include <iostream>
#include <queue>
#include <unordered_map>
using namespace std;

// A Huffman Tree node
struct Node {
    char ch;
    int freq;
    Node *left, *right;

    Node(char character, int frequency) : ch(character), freq(frequency), left(nullptr), right(nullptr) {}
};

// Comparison object to order nodes by frequency in the priority queue
struct Compare {
    bool operator()(Node* left, Node* right) {
        return left->freq > right->freq;
    }
};

// Recursive function to print Huffman codes for each character
void printCodes(Node* root, string str) {
    if (!root) return;

    // If this is a leaf node, then it contains a character
    if (!root->left && !root->right) {
        cout << root->ch << ": " << str << endl;
    }

    // Traverse left and right children
    printCodes(root->left, str + "0");
    printCodes(root->right, str + "1");
}

// Function to build the Huffman Tree and generate codes
void buildHuffmanTree(const unordered_map<char, int>& freq) {
    // Priority queue to store nodes based on frequency
    priority_queue<Node*, vector<Node*>, Compare> minHeap;

    // Create a leaf node for each character and push it into the priority queue
    for (auto pair : freq) {
        minHeap.push(new Node(pair.first, pair.second));
    }

    // Iterate while the size of the heap is not 1
    while (minHeap.size() > 1) {
        // Remove the two nodes of highest priority (lowest frequency)
        Node* left = minHeap.top(); minHeap.pop();
        Node* right = minHeap.top(); minHeap.pop();

        // Create a new internal node with a frequency equal to the sum of the two nodes
        Node* sum = new Node('\0', left->freq + right->freq);
        sum->left = left;
        sum->right = right;

        // Add the new node to the min heap
        minHeap.push(sum);
    }

    // Root of the Huffman Tree
    Node* root = minHeap.top();

    // Print Huffman codes using the Huffman Tree
    printCodes(root, "");
}

int main() {
    // Example character frequencies
    unordered_map<char, int> freq = {
        {'a', 5}, {'b', 9}, {'c', 12}, {'d', 13}, {'e', 16}, {'f', 45}
    };

    buildHuffmanTree(freq);

    return 0;
}