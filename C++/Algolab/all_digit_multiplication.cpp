#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  // @numOfTest is the number of test case.
  int numOfTest;
  cin >> numOfTest;

  int result[numOfTest];
  for(int i = 0; i < numOfTest; i++) {
    unsigned int inputNum;
    cin >> inputNum;
    // @multiple is a multiplied number.
    unsigned int multiple = inputNum;
    unsigned int tmp;
    unsigned int tmpResult;
    while (multiple / 10 != 0){
      tmp = multiple;
      tmpResult = 1;
      while (tmp / 10 != 0){
        if (tmp%10 != 0) {
          tmpResult *= (tmp % 10);
        }
        tmp /= 10;
      }
      if (tmp%10 != 0)  tmpResult *= tmp;
      multiple = tmpResult;
    }
    result[i] = multiple;
  }

  // print result.
  for (int j = 0; j < numOfTest; j++) {
    cout << result[j] << endl;
  }

  return 0;
}
