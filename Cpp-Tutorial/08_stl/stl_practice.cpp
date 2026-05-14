#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

struct Numbers
{
    int id;
};

int main()
{
    std::vector<Numbers> numbers = {{86}, {34}, {30}, {2}, {2}};

    // Adjacent elements are compared with Standard Library function
    auto it = std::adjacent_find(
        numbers.begin(),
        numbers.end(),
        [](const Numbers &n1, const Numbers &n2)
        {
            if (n1.id > n2.id)
            {
                // std::cout << n1.id << " is greater than " << n2.id << "\n";
            }
            else
            {
                // std::cout << n1.id << " is lesser than " << n2.id << "\n";
            }

            return n1.id > n2.id;
        });

    // Check all the elements for the condition -> Return True if all are present for
    // the condition only other wise false
    if (std::all_of(
            numbers.begin(),
            numbers.end(),
            [](const Numbers &n1)
            {
                return n1.id % 2 == 0;
            }))
    {
        // std::cout << "All the elements are even numbers.\n";
    }
    else
    {
        // std::cout << "Not all the elements are even numbers.\n";
    }

    // any_of check all the elements -> Return true if atleast One element satisfies
    if (std::any_of(
            numbers.begin(),
            numbers.end(),
            [](const Numbers &n1)
            {
                return n1.id % 2 == 0;
            }))
    {
        // std::cout << "Atleast one element is even number";
    }
    else
    {
        // std::cout << "No elements are even numbers";
    }

    // Binary Search
    std::list<int> list = {1, 2, 3, 4, 5, 56};

    if (std::binary_search(
            list.begin(),
            list.end(),
            56,
            [](int n1, int n2)
            {
                int v1 = std::abs(n1);
                int v2 = std::abs(n2);

                if (v1 < 0)
                    v1 = -v1;
                if (v2 < 0)
                    v2 = -v2;
                return v1 < v2;
            }))
    {
        // std::cout << "Element found in the vector\n";
    }
    else
    {
        // std::cout << "Element not found in the vector\n";
    }

        return 0;
}