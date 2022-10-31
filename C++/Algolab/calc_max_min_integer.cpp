#include <iostream>
#include <sstream>
using namespace std;

int main() {

  // @num_case is the number of test case.
  int num_case;
  cin >> num_case;
  // @num_case must be 1 <= cnt <= 100.
  if (!(1 <= num_case && num_case <= 100)){
    return 0;
  }

  // @result stores max, min integers.
  // @result[n][0] is max, @result[n][1] is min.
  int result[num_case][2];

  for (int i = 0; i < num_case; i++){

    // @cnt is the number of integers to be given.
    int cnt;
    cin >> cnt;

    // @numlist stores given numbers.
    int numlist[cnt];

    // Read line.
    string tmpstring;
    cin.ignore();
    getline(cin, tmpstring);

    // slice space in tmpstirng.
    stringstream ss(tmpstring);
    ss.str(tmpstring);
    string number;
    int tmpcnt = 0;
      while(ss >> number) {
        // convert @number string to integer and store in @numlist.
           numlist[tmpcnt] = stoi(number);
           tmpcnt += 1;
           if (tmpcnt > cnt) {break;}
         }

    int max = numlist[0];
    int min = numlist[0];

    for (int j = 0; j < cnt; j++) {
      if (max < numlist[j]) {max = numlist[j];}
      if (min > numlist[j]) {min = numlist[j];}
    }

    result[i][0] = max;
    result[i][1] = min;
  }

  // print values in @result.
  for (int i = 0; i < num_case; i++) {
    cout << result[i][0] << ' ' << result[i][1] << endl;
  }

}
