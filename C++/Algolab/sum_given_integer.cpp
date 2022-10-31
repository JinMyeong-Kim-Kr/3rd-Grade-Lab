#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {

  // @result_num is the number of result integers.
  int result_num;
  cin >> result_num;
  // @result_num must be 1 <= cnt <= 100.
  if (!(1 <= result_num && result_num <= 100)){
    return 0;
  }

  // @result is arrays to store the resulting values.
  int result[result_num];

  for (int i = 0; i < result_num; i++){
    // @cnt is the number of integers to be calculated.
    int cnt;
    cin >> cnt;

    // @cal_result stores calculated number.
    int cal_result = 0;

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
        // convert @number string to integer and store in @cal_result.
           cal_result += stoi(number);
           tmpcnt += 1;
           if (tmpcnt > cnt) {break;}
         }
      // store @cal_result in @result_num[i].
      result[i] = cal_result;
    }


  // print values in @result.
  for (int i = 0; i < result_num; i++) {
    cout << result[i] << endl;
  }
}
