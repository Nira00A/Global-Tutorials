#include <iostream> //This is a iostream library

using namespace std;

int main()
{
    int score;
    score = 100;

    int count = 10;

    // Unchangeable constant variable
    const double pi = 3.14159;

    // pi = 3.14; // This will cause a compile-time error

    cout << "Score: " << score << endl;
    cout << "Count: " << count << endl;
    cout << "Pi: " << pi << endl;
    return 0;
}