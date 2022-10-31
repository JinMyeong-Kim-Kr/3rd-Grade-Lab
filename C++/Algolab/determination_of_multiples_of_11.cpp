#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
    // @numOfTest is the number of test case.
    int numOfTest;
    cin >> numOfTest;

    string number;
    char last_digit;
    int int_number, int_last_digit;
    int idx, size;
    for (int i = 0; i < numOfTest; i++){

        cin >> number;
        if(number.size() == 1 || (number[0] == '0' && number.size() == 1))  cout << 0 << endl;
        else{
            char answer[number.size() - 1];
            idx = number.size() - 2;
            // @size is the number of @answer size.
            size = number.size() - 1;
            
            while(number.size() > 2){
                
                last_digit = number[number.size() - 1];
                answer[idx] = last_digit;
                idx--;

                number = number.substr(0, number.size() - 1);

                int_last_digit = last_digit - '0';
                int_number = number[number.size() - 1] - '0';

                if(int_number - int_last_digit > -1) {
                    int_number -= int_last_digit;

                    // change calculated last number.
                    number[number.size() - 1] = (char)(int_number + 48);
                }
                else {
                    int_number = 10 + int_number - int_last_digit;
                    number[number.size() - 1] = (char)(int_number + 48);

                    for (int idx = number.size() - 2; idx > -1; idx--) {
                        if(number[idx] == '0') {
                            number[idx] = '9';
                        } 
                        else {
                            int_number = number[idx] - '0';
                            number[idx] = (char)((int_number - 1) + 48);
                            if(idx == 0 && number[idx] == '0')  number = number.substr(1, number.size());
                            break; 
                            }
                    }
                }   
            }
        
        int_number = number[0] - '0';
        int_last_digit = number[1] - '0';
        
        if(int_number - int_last_digit == 0) {
            answer[0] = (char)(int_last_digit + 48);
            for (int k = 0; k < size; k++){
                cout << answer[k];
            } 
            cout << endl;
        }  
        else cout << 0 << endl;
        }

    }



}