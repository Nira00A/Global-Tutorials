#include <iostream> //This is a iostream library

using namespace std;

int main()
{
    float tea_price = 2.99;
    int rounded_price = (int)tea_price; // C-style cast, truncates the decimal part

    cout << "Tea Price: $" << tea_price << endl;
    cout << "Rounded Price: $" << rounded_price << endl;

    return 0;
};