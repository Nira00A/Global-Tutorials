#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

int total_chai_served(int chai[], int size)
{
    int total = 0;
    for (int i; i < size; i++)
    {
        total += chai[i];
    }
    return total;
}

int main()
{
    int chai_served[3] = {22, 33, 44};

    int total = total_chai_served(chai_served, 3);

    return 0;
}