#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  // @num_of_test is the number of test case.
  int num_of_test;
  cin >> num_of_test;

  int overlap_length, section_length;
  int sec1_x1, sec1_x2, sec2_x1, sec2_x2;
  for (int i = 0; i < num_of_test; i++){
    cin >> sec1_x1 >> sec1_x2 >> sec2_x1 >> sec2_x2;
    // two sections do not overlap
    if(sec1_x2 < sec2_x1 || sec2_x2 < sec1_x1) {overlap_length = 0; section_length = (sec1_x2 - sec1_x1) + (sec2_x2 - sec2_x1);
    cout << overlap_length << " " << section_length << endl; continue;}
    // an interval exists inside
    else if(sec1_x1 < sec2_x1 && sec2_x2 < sec1_x2) {overlap_length = sec2_x2 - sec2_x1; section_length = sec1_x2 - sec1_x1;}
    else if(sec2_x1 < sec1_x1 && sec1_x2 < sec2_x2) {overlap_length = sec1_x2 - sec1_x1; section_length = sec2_x2 - sec2_x1;}
    // two sections overlap
    else if(sec1_x2 < sec2_x2) {section_length = sec2_x2 - sec1_x1;}
    else if(sec2_x2 < sec1_x2) {section_length = sec1_x2 - sec2_x1;}
    if (sec1_x1 < sec2_x1 && sec1_x2 < sec2_x2) {overlap_length = sec1_x2 - sec2_x1;}
    else if(sec2_x1 < sec1_x1 && sec2_x2 < sec1_x2) {overlap_length = sec2_x2 - sec1_x1;}
    cout << overlap_length << " " << section_length << endl;
  }


  return 0;
}
