#include <iostream>

int main()
{
    int age;
    std::string name;

    std::cout << "Please enter your name :" << std::endl;
    std::cin >> name;

    std::cout << "Please enter your age : " << std::endl;
    std::cin >> age;

    /*Grabbing the data in one go
        syd::cin >> name >> int
    */

    return 0;
}