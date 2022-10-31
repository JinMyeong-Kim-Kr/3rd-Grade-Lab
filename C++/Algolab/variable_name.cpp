#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    // @num_of_test is the number of test case.
    int num_of_test;
    cin >> num_of_test;

    // @name is a variable name.
    string name;

    // @state is a boolean variable indicating whether variable name is available.
    bool state;

    for (int i = 0; i < num_of_test; i++){
        cin >> name;
        state = true;
        for(int j = 0; j < name.size(); j++){
            
            // The first index character is false if it is numeric.
            if(j == 0 && (48 <= name[j] && name[j] <= 57)){
                state = false;
                break;
            }
            // If the letter is not an English letter, a number, or _, it is false.
            else if( !((65 <= name[j] && name[j] <= 90) || (97 <= name[j] && name[j] <= 122) || (name[j] == '_') || (48 <= name[j] && name[j] <= 57)))  {
                state = false;
                break;
                }
        }
        cout << state << endl;
    }
    
    return 0;
}
