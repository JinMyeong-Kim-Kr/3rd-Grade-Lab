#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  // @num_of_test is the number of test case.
  int num_of_test;
  cin >> num_of_test;

  // @num_of_digits is the number of digits to be input.
  int num_of_digits;
  // @cnt is the number of occurrences of intermediate high points.
  int cnt;

  int high_point, digit;
  bool low_to_high;
  for (int i = 0; i < num_of_test; i++){
    cnt = 0; high_point = 0;
    low_to_high = 0;

    cin >> num_of_digits;
    for (int j = 0; j < num_of_digits; j++){
      cin >> digit;
      if (j == 0) high_point = digit;
      if(digit > high_point){
        high_point = digit;
        low_to_high = 1;
      }
      else if(digit < high_point){
        // Intermediate high point occurrence.
        if(low_to_high) {
          high_point = digit;
          cnt += 1;
          low_to_high = 0;
        }
        else{
          high_point = digit;
          low_to_high = 0;
        }
      }
    }
    // print result.
    cout << cnt << endl;
  }
  return 0;
}
