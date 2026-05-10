#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    int chai_temp[5] = {58, 50, 74, 13, 58};

    cout << "Chai Temperature\n";
    for (int i = 0; i < 5; i++)
    {
        cout << "Temp : " << i << endl;
    }

    return 0;
}