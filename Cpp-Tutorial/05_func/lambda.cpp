#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    // lambda
    auto prepared_chai = [](int cups)
    {
        cout << "Preparing " << cups << endl;
    };

    prepared_chai(4);

    return 0;
}