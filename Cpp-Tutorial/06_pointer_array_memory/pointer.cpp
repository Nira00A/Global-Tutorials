#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int *prepare_orders(int cups)
{
    int *orders = new int[cups];
    for (int i = 0; i < cups; i++)
    {
        orders[i] = i + 1;
    }
    return orders;
}

int main()
{
    int cups = 3;
    int *orders = prepare_orders(cups);

    for (int i = 0; i < cups; i++)
    {
        cout << "Order : " << orders[i] << endl;
    }

    // Clean up the dynamically allocated memory
    delete[] orders;

    return 0;
}