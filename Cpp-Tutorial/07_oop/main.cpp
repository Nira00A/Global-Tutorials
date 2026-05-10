#include <iostream> //This is a iostream library
#include <string>   //This is a string library
#include <vector>   //This is a vector library

using namespace std;

class Chai
{
    // By default, members of a class are private
public:
    string tea_name;            // name of the tea
    int servings;               // number of servings
    vector<string> ingredients; // list of ingredients

    // Member functions
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

    masala_chai.tea_name = "Masala Chai";
    masala_chai.servings = 2;
    masala_chai.ingredients = {"Water", "Milk", "Tea Leaves", "Sugar", "Spices"};
    masala_chai.display_ingredients();

    cout << "Tea Name: " << masala_chai.tea_name << endl;
    cout << "Servings: " << masala_chai.servings << endl;

    Chai green_tea;

    green_tea.tea_name = "Green Tea";
    green_tea.servings = 1;
    green_tea.ingredients = {"Water", "Green Tea Leaves"};
    green_tea.display_ingredients();

    cout << "Tea Name: " << green_tea.tea_name << endl;
    cout << "Servings: " << green_tea.servings << endl;

    return 0;
}