// Convert command line values to double
#include <iostream>
#include <string> // provides stoX where X can be i (int), d (double), etc.

using namespace std;
int main(int argc, char const *argv[])
{

    for (int i=1; i<argc ; i++)
    {    
        cout << i << " ";
        try 
        {
            double v = stod(argv[i]);  
            cout << v << endl;
            continue;
        }
        catch (...)
        {
            cout << argv[i] << " is not a double.";
        }
        cout << endl;
    }
}
