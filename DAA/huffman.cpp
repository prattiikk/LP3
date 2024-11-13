#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <string>

using namespace std;

class node
{
public:
    char data;
    int freq;
    node *left;
    node *right;
    node(char data, int freq)
    {
        this->data = data;
        this->freq = freq;
        this->left = this->right = nullptr;
    }
};

void printCodes(node *root, string str, unordered_map<char, string> &codes)
{
    if (root == nullptr)
        return;

    if (root->data != '$') // Only assign codes to leaf nodes
    {
        codes[root->data] = str;
    }

    // Recursive traversal
    printCodes(root->left, str + "0", codes);
    printCodes(root->right, str + "1", codes);
}

struct Compare
{
    bool operator()(node *left, node *right)
    {
        return left->freq > right->freq;
    }
};

void generateHuffTree(vector<char> &data, vector<int> &freq, int n)
{
    priority_queue<node *, vector<node *>, Compare> pq;

    for (int i = 0; i < n; i++)
    {
        pq.push(new node(data[i], freq[i]));
    }

    while (pq.size() > 1)
    {
        node *left = pq.top();
        pq.pop();
        node *right = pq.top();
        pq.pop();

        node *temp = new node('$', left->freq + right->freq);
        temp->left = left;
        temp->right = right;
        pq.push(temp);
    }

    unordered_map<char, string> codes;
    printCodes(pq.top(), "", codes);

    cout << "Generated codes: " << endl;
    for (auto temp : codes)
    {
        cout << temp.first << " : " << temp.second << endl;
    }
}

int main()
{
    int n;
    cout << "Enter the Number of chars: ";
    cin >> n;
    vector<char> data(n);
    vector<int> freq(n);
    for (int i = 0; i < n; i++)
    {
        cout << "Enter the char: ";
        cin >> data[i];
        cout << "Enter the freq of that char: ";
        cin >> freq[i];
    }

    generateHuffTree(data, freq, n);
    return 0;
}