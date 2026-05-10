#include <iostream> //This is a iostream library
#include <string>   //This is a string library
using namespace std;

int main()
{
    string tea_order;
    cout << "What type of tea would you like to order? \n";
    cin >> tea_order; // Read user input for tea order

    if (tea_order == "Green")
    {
        tea_order = "Green Tea";
        cout << "You ordered " << tea_order << "." << endl;
    }
    else if (tea_order == "Black Tea")
    {
        tea_order = "Black Tea";
        cout << "You ordered " << tea_order << "." << endl;
    }
    else
    {
        cout << "Sorry, we don't have that type of tea." << tea_order << endl;
    }

    return 0;
};