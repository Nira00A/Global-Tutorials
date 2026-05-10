# This is the summary of the tutorial
In this Tutorial I will learn cpp thats all

## Compiler used
### We are using C:/MinGW/bin/g++.exe and C:/MinGW/bin/clang.exe

## How to run the code?
1. First need to configure the project file by going to Terminal > Configure Task...
2. Select the g++ or clang.exe as a compiler
3. After than when you want to run the code -> Select the file you want to run -> Go to Terminal (in the top) -> Run Task... -> select the complier you configured with.
4. Now an exe file will create accourding to the file name.
5. Just use ./${name}.exe in the bottom terminal to run the file.

## So first the print like statement
we need to import a module for it which is 
**#include < iostream >**

## Ultimate thing happening is 
cpp code -> compiler -> Excutable binary file

## 3 types error in CPP
1. Compile time error
2. Runtime error 
3. Warning

## What is Cpp?What type of program it is?
1. A statement is a basic unit of computation in a C++ program
2. Every C++ program is a collection of statements organized in a certain way to achieve some goal.
3. Statements end wirh a semicolon in C++( ; )

## Functions and Variables 
### How to write a function in Cpp:
This is the code:
<pre>
    int addition(int firstNumber, int secondNumber){
        int sum = firstNumber + secondNumber;
        return sum;
    };
</pre>

### How to make a variable
This is the code:
<pre>
    int x = 13
        OR
    int x {13}
</pre>

### How to print statements
This is the code:
<pre>
    std::cout << "The sum is : " << firstNumber + secondNumber << std::endl;
    std::cout << "The sumFunction is : " << sumFunction << std::endl;
</pre>

std::cout -> Printing data to the console
std::cin -> Reading data from the terminal
std::ceer -> Printing errors to the console
std::clog -> Printing log message to the console

example of Printing data:
<pre>
    //for errors 

    std::cerr << "std::cerr output : Something went wrong" << std::endl;

    // for logs
    std::clog << "std::clog output : This is the log message" << std::endl
</pre>



### Input / output 
## Thesyntax of input of output




