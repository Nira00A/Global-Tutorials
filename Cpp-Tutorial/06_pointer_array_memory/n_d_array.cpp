#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int main()
{
    int chai_sales[3][3] = {
        {22, 33, 44},
        {55, 66, 77},
        {88, 99, 11}};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << "Sales : " << chai_sales[i][j] << endl;
        }
    }

    return 0;
}