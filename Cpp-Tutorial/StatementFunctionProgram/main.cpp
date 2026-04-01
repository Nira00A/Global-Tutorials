#include <iostream> //This is a iostream library

int addition(int firstNumber, int secondNumber){
    int sum = firstNumber + secondNumber;
    return sum;
};

int main(){
    int firstNumber{3};
    int secondNumber{7};

    int sumFunction = addition(firstNumber, secondNumber);

    std::cout << "The sum is : " << firstNumber + secondNumber << std::endl;
    std::cout << "The sumFunction is : " << sumFunction << std::endl;

    return 0;
};