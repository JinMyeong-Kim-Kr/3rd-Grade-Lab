#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    // @num_of_test is the number of test case.
    int num_of_test;
    cin >> num_of_test;

    int size;
    int interval;
    int tmp;
    for (int i = 0; i < num_of_test; i++){
        cin >> size;
        // @square_array is a square array to output.
        char sqaure_array[size][size];

        // @interval is the interval number between '\' and '/'.
        interval = size - 3;

        // @j is row, @k is column.
        for(int j = 0; j < size; j++){
            if(j == size / 2) {interval += 2; tmp += 2;}
            for(int k = 0; k < size; k++){
                // case: '-', '+'
                if (j == 0 || j == size / 2 || j == size  - 1){
                    // case: '+'
                    if (k == 0 || k == size / 2 || k == size - 1){sqaure_array[j][k] = '+';}
                    // case: '-'
                    else {sqaure_array[j][k] = '-';}
                } // case: '|', '\', '/'
                else {
                    // case: '|'
                    if (k == 0 || k == size / 2 || k == size - 1) {sqaure_array[j][k] = '|';}
                    // case : '\' , '/'
                    else if (j < size / 2){
                        if (k == j) {sqaure_array[j][k] = '\\'; tmp = k;}
                        else if (k == tmp + interval) {sqaure_array[j][k] = '/'; interval -= 2;}
                         // case : '.'
                        else {sqaure_array[j][k] = '.';}
                    }
                    else if (j > size / 2){
                        // case : '\'
                        if (k == j) {sqaure_array[j][k] = '\\'; tmp = k + 1;}
                        // case : '/'
                        else if (k == tmp - interval) {sqaure_array[j][k] = '/'; interval += 2;}
                         //: '.'
                        else {sqaure_array[j][k] = '.';}
                    }
                   
                }
            }
            // case: '*'
            sqaure_array[size / 2][size / 2] = '*';
        } // end of loop.

        // print result.
        for (int p = 0; p < size; p++){
            for (int q = 0; q < size; q++){
                cout << sqaure_array[p][q];
            }
            cout << endl;
        }

    }
    
    
    return 0;
}
