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

    // parameter constructor
    Chai(string name, int serv, vector<string> ingredients_list)
    {
        tea_name = name;
        servings = serv;
        ingredients = ingredients_list;
        cout << "Parameterized constructor called for " << tea_name << endl;
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
    Chai masala_chai("Masala Chai", 2, {"Water", "Tea leaves", "Milk"});

    masala_chai.display_ingredients();

    // copy the object
    Chai copied_chai = masala_chai;
    copied_chai.display_ingredients();

    return 0;
}