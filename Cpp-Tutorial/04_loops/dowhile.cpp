#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    string response;

    // First do then ask the user and accourding to user manupulate the do statement
    do
    {
        cout << "Do you want more tea (yes/no): ";
        getline(cin, response);
    } while (response != "no" && response != "No");

    return 0;
}