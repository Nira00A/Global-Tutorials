#include <iostream>

int main()
{
    // Complie time error without ";"
    std::cout << "Hello World" << std::endl;
    return 0;

    // Run time error
    int value = 7 / 0;
    std::cout << value << std::endl;
    return 0;
}