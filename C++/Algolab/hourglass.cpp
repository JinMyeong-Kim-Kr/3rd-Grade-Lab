#include <iostream>
using namespace std;

int main() {
  int cnt;
  cin >> cnt;

  // @k is the height of the hourglass.
  int k;

  string tmp;
  for (int c = 0; c < cnt; c++){
    cin >> k;

    // @k is odd number, 3 <= k <= 99.
    if (k%2 == 0) {
      return 0;
    }
    else if (!(3 <= k && k <= 99)) {
      return 0;
    }

    for (int i = 0; i <= k/2; i++){

      // Print first line.
      if (i == 0){
        for (int j = 0; j < k; j++){
          if(j % 2 == 0) {
            tmp += '*';
          }
          else {
            tmp += '+';
          }
        }
      }
      // Print middle.
      else {
        for (int t = 0; t < i; t++) {
          tmp += '-';
        }
        for (int m = 0; m < k - i*2; m++){
          if (m % 2 == 0) {
            tmp += '*';
          }
          else {
            tmp += '+';
          }
      }
      for (int t = 0; t < i; t++) {
        tmp += '-';
        }
      }
      tmp += '\n';
    }

    // Print rest.
    for (int i = k/2 - 1; i >= 0; i--){
      // Print last line.
      if (i == 0){
        for (int j = 0; j < k; j++){
          if(j % 2 == 0) {
            tmp += '*';
          }
          else {
            tmp += '+';
          }
        }
      }
      // Print middle.
      else {
        for (int t = 0; t < i; t++) {
          tmp += '-';
        }
        for (int m = 0; m < k - i*2; m++){
          if (m % 2 == 0) {
            tmp += '*';
          }
          else {
            tmp += '+';
          }
        }
        for (int t = 0; t < i; t++) {
          tmp += '-';
        }
      }
      tmp += '\n';
    }
  }
      cout << tmp;

  }
