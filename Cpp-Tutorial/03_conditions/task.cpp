#include <iostream> //This is a iostream library
#include <string>   //This is a string library
using namespace std;

int main()
{
    int choice;
    double price;

    cout << "Welcome to the Tea Shop! Please select a tea type:\n";
    cout << "1. Green Tea\n";
    cout << "2. Black Tea\n";
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;

    switch (choice)
    {
    case 1:
        choice = 1;
        price = 19.00;
        cout << "You have choosed Green tea of price :" << price << endl;
        break;
    case 2:
        choice = 2;
        price = 9.00;
        cout << "You have choosed Black Tea" << price << endl;
        break;
    default:
        cout << "Invalid Choice" << price << "\n Choice number: " << choice << endl;
        break;
    }

    return 0;
};