#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    int tea_cups;

    cout << "Enter the number of tea cups you want: \n";
    cin >> tea_cups;

    // while loop
    while (tea_cups > 0)
    {
        cout << "Serving a cup of tea \n"
             << tea_cups << " remaining " << endl;
        tea_cups--;
    }

    cout << "Done";

    return 0;
}