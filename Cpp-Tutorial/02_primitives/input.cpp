#include <iostream> //This is a iostream library

using namespace std;

int main()
{
    string user_tea;
    int tea_quantity;

    cout << "Enter the type of tea you want: \n";
    getline(cin, user_tea); // Read the entire line of input for tea type

    // ask for quantity
    cout << "Enter the quantity of tea you want: \n";
    cin >> tea_quantity; // Read the quantity of tea

    cout << "You ordered " << tea_quantity << " cups of " << user_tea << "." << endl;

    return 0;
};