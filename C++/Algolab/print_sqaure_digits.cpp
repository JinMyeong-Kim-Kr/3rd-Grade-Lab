#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  // @num_case is the number of test case.
  int num_case;
  cin >> num_case;

  for (int i = 0; i < num_case; i++){

  // @square_size is the number of size of square.
  int square_size;
    cin >> square_size;

    // @square is an array of square.
  int square[square_size][square_size];

    square[square_size/2][square_size/2] = 0;
    int cnt = 0;
    int corner = square_size / 2 - 1;
    int length = 2;
    int printnum = 1;
    while (cnt < square_size/2) {
      // top of square.
      for(int j = 0; j < length; j++){
        square[corner][corner + j] = printnum;
      }
      // right of square.
      for(int k = 0; k < length; k++){
        square[corner + k][corner + length] = printnum;
      }
      // bottom of square.
      for(int l = 0; l < length; l++){
        square[corner + length][corner + 1 + l] = printnum;
      }
      // left of square.
      for (int m = 0; m < length; m++){
        square[corner + 1 + m][corner] = printnum;
      }
      if (printnum == 1)  {printnum = 0;} else {printnum = 1;}
      cnt++;
      corner--;
      length += 2;
    } // end of while.

    // print result.
    for (int p = 0; p < square_size; p++){
      for (int q = 0; q < square_size; q++){
        cout << square[p][q];
      }
      cout << endl;
    }
      // end of for loop.
  }
  return 0;
}
