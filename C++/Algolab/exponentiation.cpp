#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
  // @num_case is the number of test case.
  int num_case;
  cin >> num_case;

  // @result[] is an array of result values.
  int result[num_case];

  for (int i = 0; i < num_case; i++){
    // @num is the number of string types to be calculated.
    int num;
    cin >> num;

    // @cnt is number of digits.
    int cnt = 0;
    unsigned long int sum = 0;
    int tmp = num;
    while (tmp / 10 != 0){
      result[cnt] = tmp % 10;
      tmp /= 10;
      cnt++;
    }
    result[cnt] = tmp % 10;

    for(int j = 0; j <= cnt; j++){
      tmp = result[j];
      for (int k = 0; k < cnt; k++){
        result[j] *= tmp;
      }
      sum += result[j];
    }

    if (sum == num) {
      cout << "1" << endl;
    }
    else {
      cout << "0" << endl;
    }

  }
  return 0;
}
