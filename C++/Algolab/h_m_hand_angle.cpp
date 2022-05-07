#include <iostream>
using namespace std;


int angleClock(int h, int m);

int main(int argc, char const *argv[]) {

  // @numOfTest is the number of test case.
  int numOfTest;
  cin >> numOfTest;

  int hour, minute;
  for(int i = 0; i < numOfTest; i++){
    cin >> hour >> minute;
    cout << angleClock(hour, minute) << endl;
  }
  return 0;
}

// angleClock calculate the angle between the hour hand and the minute hand.
int angleClock(int h, int m) {
  float hourAngle = h*30 + 0.5*m;
  float minuteAngle = m*6;
  float angle;

  angle = abs(hourAngle - minuteAngle);
  if(angle > 180) {angle = 360 - angle;}

  return int(angle);
}
