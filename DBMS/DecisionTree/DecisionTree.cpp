#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct DataPoint
{
    vector<double> features;
    int label;
};

class DecisionTree
{
private:
    struct Node
    {
        int feature_index;
        double threshold;
        Node *left;
        Node *right;
        int label;
    };

    Node *root;

public:
    DecisionTree()
    {
        root = nullptr;
    }

    void fit(const vector<DataPoint> &data)
    {
        root = build_tree(data);
    }

    int predict(const vector<double> &x)
    {
        Node *current = root;
        while (current->left != nullptr && current->right != nullptr)
        {
            if (x[current->feature_index] < current->threshold)
                current = current->left;
            else
                current = current->right;
        }
        return current->label;
    }

private:
    Node *build_tree(const vector<DataPoint> &data)
    {
        if (data.empty())
            return nullptr;

        // Find the best feature and threshold to split the data
        int feature_index = 0;
        double threshold = 0;
        double max_gain = 0;

        for (int i = 0; i < data[0].features.size(); i++)
        {
            for (const auto &point : data)
            {
                double gain = calc_information_gain(data, i, point.features[i]);
                if (gain > max_gain)
                {
                    feature_index = i;
                    threshold = point.features[i];
                    max_gain = gain;
                }
            }
        }

        // Split the data into subsets
        vector<DataPoint> left_data, right_data;
        for (const auto &point : data)
        {
            if (point.features[feature_index] < threshold)
                left_data.push_back(point);
            else
                right_data.push_back(point);
        }

        // Create a new node for the split
        Node *node = new Node();
        node->feature_index = feature_index;
        node->threshold = threshold;

        // Recursively build the left and right subtrees
        node->left = build_tree(left_data);
        node->right = build_tree(right_data);

        return node;
    }

    double calc_information_gain(const vector<DataPoint> &data, int feature_index, double threshold)
    {
        // Calculate the information gain using the chosen feature and threshold
        //...
    }
};

int main()
{
}