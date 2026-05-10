#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    string teaTypes[3] = {"Green Tea", "Black Tea", "Lemon Tea"};

    for (int i = 0; i < 3; i++)
    {
        if (teaTypes[i] == "Black Tea")
        {
            continue; // Skip the rest of the loop and move to the next iteration
        }
        cout << "Brewing: " << teaTypes[i] << endl;
    }

    return 0;
}