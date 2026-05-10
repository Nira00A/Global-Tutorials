#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

// call by value function
void pour_chai(int cups)
{
    cups += 5;
    cout << "Pouring " << cups << " cups of chai." << endl;
}

// call by reference function
void pour_chai_ref(int &cups)
{
    cups += 5;
    cout << "Pouring " << cups << " cups of chai." << endl;
}

int main()
{
    int cups = 2;
    // call by value: the value of cups is passed to the function,
    // and any changes made to cups inside the function will not
    // affect the original variable in main
    pour_chai(cups);
    cout << "Cups after pouring: " << cups << endl; // cups will still be 2, because it's passed by value

    // call by reference: the reference to cups is passed to the function,
    // and any changes made to cups inside the function will affect the original variable in main
    pour_chai_ref(cups);
    cout << "Cups after pouring (by reference): " << cups << endl;
    return 0;
}