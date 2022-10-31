#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  // @num_case is the number of test case.
  int num_case;
  cin >> num_case;

  // @square_size is the number of size of square.
  int square_size;
  // @num is a number to fill in @square.
  int num;
  // @idx is an index of @square.
  int idx;
  // @start is an index of start point.
  int start;
  // @end is an index of end.
  int end;
  for (int i = 0; i < num_case; i++){
    cin >> square_size >> start >> end;
    // @square is an array of snail-orderd square.
    int square[square_size][square_size];
    // @result is an array of snail-ordered numbers.
    int result[square_size*square_size];

    num = 1;
    // fill number in @square.
    for (int p = 0; p < square_size; p++){
      for (int q = 0; q < square_size; q++){
        square[p][q] = num;
        num += 1;
      }
    }

    int cnt = 0;
    int corner;
    int length;
    if(square_size % 2 == 0){
      idx = 0;
      length = square_size - 1;
      while (cnt < square_size/2) {
        // snail sequence : top -> right -> bottom -> left ...
        // top of square.
        for(int j = 0; j < length; j++){
          result[idx] = square[cnt][cnt + j];
          idx++;
        }
        // right of square.
        for(int k = 0; k < length; k++){
          result[idx] = square[cnt + k][cnt + length];
          idx++;
        }
        // bottom of square.
        for (int m = length; m > 0; m--){
          result[idx] = square[cnt + length][cnt + m];
          idx++;
        }

        // left of square.
        for(int l = length; l > 0; l--){
          result[idx] = square[cnt + l][cnt];
          idx++;
        }
        cnt++;
        length -= 2;
      } // end of while.
    }
    else{
      // middle of @square.
      length = 2;
      idx = square_size*square_size - 1;
      result[idx] = square[square_size/2][square_size/2];
      idx--;
      corner = square_size / 2 - 1;
    while (cnt < square_size/2) {
      // snail sequence : center -> left -> bottom -> right -> top -> left ...
      // left of square.
      for (int m = 0; m < length; m++){
        result[idx] = square[corner + 1 + m][corner];
        idx--;
      }

      // bottom of square.
      for(int l = 0; l < length; l++){
        result[idx] = square[corner + length][corner + 1 + l];
        idx--;
      }

      // right of square.
      for(int k = length - 1; k > -1; k--){
        result[idx] = square[corner + k][corner + length];
        idx--;
      }

      // top of square.
      for(int j = length - 1; j > -1; j--){
        result[idx] = square[corner][corner + j];
        idx--;
      }
      cnt++;
      corner--;
      length += 2;
    } // end of while.
  }
    //print result.
    for(int p = start - 1; p < end; p++) cout << result[p] << " ";
    cout << endl;
  } // end of for loop.

  return 0;
}
