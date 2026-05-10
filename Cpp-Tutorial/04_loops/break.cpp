#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    string response;

    while (true)
    {
        cout << "Do you want more tea? ";
        getline(cin, response);

        if (response == "stop")
        {
            // exit the loop
            break;
        }

        cout << "Here is your another cup of tea.\n";
    }

    cout << "No more cups of tea" << endl;

    return 0;
}