#include <iostream> //This is a iostream library

using namespace std;

int main()
{
    int tea_leaves = 50;
    float water_temperature = 200.5;
    double price_of_tea = 2.99;
    char tea_type = 'G';
    bool is_tea_ready = true;

    cout << "Tea Leaves: " << tea_leaves << endl;
    cout << "Water Temperature: " << water_temperature << " degrees" << endl;
    cout << "Price of Tea: $" << price_of_tea << endl;
    cout << "Tea Type: " << tea_type << endl;
    cout << "Is the tea ready? " << (is_tea_ready ? "Yes" : "No") << endl;

    return 0;
};