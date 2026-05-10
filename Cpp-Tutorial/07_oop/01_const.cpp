#include <iostream> //This is a iostream library
#include <string>   //This is a string library
#include <vector>   //This is a vector library

using namespace std;

class Chai
{
public:
    string tea_name;            // name of the tea
    int servings;               // number of servings
    vector<string> ingredients; // list of ingredients

    // default constructor
    Chai()
    {
        tea_name = "Unknown";
        servings = 0;
        ingredients = {"Water", "Tea leaves"};
        cout << "Default constructor called for " << tea_name << endl;
    }

    void display_ingredients()
    {
        cout << "Ingredients for " << tea_name << ":\n";
        for (string ingredient : ingredients)
        {
            cout << "- " << ingredient << endl;
        }
        cout << endl;
    }
};

int main()
{
    Chai masala_chai;

    masala_chai.display_ingredients();

    return 0;
}