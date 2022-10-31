#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  // @numOfTest is the number of test case.
  int numOfTest;
  cin >> numOfTest;

  // @result stores sorted result.
  int result[numOfTest][3];

  int num1, num2, num3;

  for (int i = 0; i < numOfTest; i++) {
    cin >> num1 >> num2 >> num3;
    if(num1 <= num2){
      if (num2 <= num3){
        // case: num1 <= num2 <= num3
        result[i][0] = num1;
        result[i][1] = num2;
        result[i][2] = num3;
      }else {
      // case: num1 <= num3 <= num2
      if(num1 <= num3) {
        result[i][0] = num1;
        result[i][1] = num3;
        result[i][2] = num2;
        }
      // case: num3 <= num1 <= num2
      else {
        result[i][0] = num3;
        result[i][1] = num1;
        result[i][2] = num2;
        }
      }
    }
    else {
      if (num3 <= num2){
        // case: num3 <= num2 <= num1
        result[i][0] = num3;
        result[i][1] = num2;
        result[i][2] = num1;
      }
    else {
      if (num1 <= num3){
        // case: num2 <= num1 <= num3
        result[i][0] = num2;
        result[i][1] = num1;
        result[i][2] = num3;
      }
      else {
        // case: num2 <= num3 <= num1
        result[i][0] = num2;
        result[i][1] = num3;
        result[i][2] = num1;
      }
    }
  }
} // end for loop.

  // print result.
  for(int j = 0; j < numOfTest; j++) {
    cout << result[j][0] << ' ' << result[j][1] << ' ' << result[j][2] << endl;
  }

  return 0;
}
