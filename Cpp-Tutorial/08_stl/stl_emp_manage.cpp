#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iterator>
#include <numeric>

using namespace std;

struct Employee
{
    int id;
    string name;
    double salary;
};

void displayEmployee(const Employee &emp)
{
    cout << "ID: " << emp.id << "Name: " << emp.name
         << "Salary: " << emp.salary << endl;
}

int main()
{

    vector<Employee> employees = {
        {101, "arin", 100000},
        {102, "abhi", 10000},
        {103, "arnab", 40000},
        {104, "aditya", 30000},
        {105, "arko", 10000},
    };

    sort(
        employees.begin(),
        employees.end(),
        [](const Employee &e1,
           const Employee &e2)
        {
            return e1.salary > e2.salary;
        });

    cout << "Employees sorted by salary -> Highest to Lowest \n";

    for_each(
        employees.begin(),
        employees.end(),
        displayEmployee);

    vector<Employee> highEarners;

    copy_if(
        employees.begin(),
        employees.end(),
        back_inserter(highEarners),
        [](const Employee &e)
        {
            return e.salary > 50000;
        });

    cout << "Employees who are high earners \n";
    for_each(
        highEarners.begin(),
        highEarners.end(),
        displayEmployee);

    double total_salary = accumulate(employees.begin(), employees.end(), 0.0, [](double sum, const Employee &e)
                                     { return sum + e.salary; });

    double average_salary = total_salary / employees.size();

    auto highest_paid = max_element(employees.begin(), employees.end(), [](const Employee &e1, const Employee &e2)
                                    { return e1.salary < e2.salary; });

    return 0;
}
