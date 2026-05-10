#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    int tea_cups = 5;

    for (int i = 1; i <= tea_cups; i++)
    {
        cout << "Brewing a cup of tea: " << i << endl;
    }

    return 0;
}