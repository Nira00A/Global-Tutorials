#include <iostream> //This is a iostream library
#include <string>   //This is a string library

using namespace std;

// function declaration
// returnType functionName(parameter1, parameter2, ...) {
//     // function body
//     // return statement (if needed)
// }

int temperature(int temp)
{
    return temp;
}

// function declaration for serve function
void serve(int cups);
void serving_tea(string tea_type = "green tea");

int main()
{
    int result = temperature(30);
    cout << "Temperature: " << result << endl;
    serve(5);
    serving_tea();
    return 0;
}

// defination of serve function
void serve(int cups)
{
    cout << "Serving " << cups << " cups of tea." << endl;
}

void serving_tea(string tea_type)
{
    cout << "Serving " << tea_type << "." << endl;
}
