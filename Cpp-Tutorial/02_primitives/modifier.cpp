#include <iostream> //This is a iostream library

using namespace std;

int main()
{
    signed int a = -10;  // signed integer can hold negative values
    unsigned int b = 20; // unsigned integer can only hold non-negative values

    long large_number = 1000000; // long can hold larger numbers than int
    double larger_double = 1000000;
    float smaller_float = 1000000;

    cout << "Signed integer: " << a << endl;
    cout << "Unsigned integer: " << b << endl;
    cout << "Large number: " << large_number << endl;
    cout << "Larger double: " << larger_double << endl;
    cout << "Smaller float: " << smaller_float << endl;

    return 0;
};