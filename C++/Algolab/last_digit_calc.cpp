#include <iostream>
#include <sstream>
using namespace std;

int main(int argc, char const *argv[]) {

  // @numOfTest is the number of test case.
  int numOfTest;
  cin >> numOfTest;
  cin.ignore();
  int result, cnt, num_cnt;
  int arrayResults[numOfTest];

  for (int i = 0; i < numOfTest; i++) {
    result = 1; cnt = 0; num_cnt = 0;

    string line;

    getline(cin, line);
    stringstream ss(line);
    ss.str(line);
    string num;
    while(ss >> num) {
      if (cnt == 0){
        // @num_cnt is the number of given digits.
        num_cnt = stoi(num);
      }
      else{
        // @result is a value of calculated last digit.
        result = (stoi(num)%10)*(result%10);
      }
      cnt += 1;
      if (cnt > num_cnt) {
        break;
      }
    }
    arrayResults[i] = result;
  }

  // print result.
  for (int j = 0; j < numOfTest; j++) {
    cout << arrayResults[j]%10 << endl;
  }




  return 0;
}
