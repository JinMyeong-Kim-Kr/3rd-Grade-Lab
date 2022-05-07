#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  // @num_of_test is the number of test case.
  int num_of_test;
  cin >> num_of_test;

  int area, perimeter;
  int p_area, p_perimeter;
  int q_area, q_perimeter;
  // (x1, y1) is the lower left coordinate of the rectangle.
  // (x2, y2) is the upper right coordinate of the rectangle.
  int p_x1, p_y1, p_x2, p_y2;
  int q_x1, q_y1, q_x2, q_y2;

  int tmp_x1, tmp_y1, tmp_x2, tmp_y2;
  for(int i = 0; i < num_of_test; i++){
    cin >> p_x1 >> p_y1 >> p_x2 >> p_y2;
    cin >> q_x1 >> q_y1 >> q_x2 >> q_y2;

    // case: the two squares do not overlap.
    if(q_y2 < p_y1 || p_y2 < q_y1 || p_x2 < q_x1 || q_x2 < p_x1) {
      p_area = (p_x2 - p_x1)*(p_y2 - p_y1);
      q_area = (q_x2 - q_x1)*(q_y2 - q_y1);

      p_perimeter = ((p_x2 - p_x1) + (p_y2 - p_y1)) * 2;
      q_perimeter = ((q_x2 - q_x1) + (q_y2 - q_y1)) * 2;

      area = p_area + q_area;
      perimeter = p_perimeter + q_perimeter;
      // print result.
      cout << area << " " << perimeter << endl;
      continue;
    } // case: one rectangle is inside.
    else if (p_x1 < q_x1 && p_y1 < q_y1 && q_x2 < p_x2 && q_y2 < p_y2){
      area = (p_x2 - p_x1)*(p_y2 - p_y1);
      perimeter = ((p_x2 - p_x1) + (p_y2 - p_y1)) * 2;
      // print result.
      cout << area << " " << perimeter << endl;
      continue;
      }
    else if (q_x1 < p_x1 && q_y1 < p_y1 && p_x2 < q_x2 && p_y2 < q_y2){
      area = (q_x2 - q_x1)*(q_y2 - q_y1);
      perimeter = ((q_x2 - q_x1) + (q_y2 - q_y1)) * 2;
      // print result.
      cout << area << " " << perimeter << endl;
      continue;
    } // case: the two squares do overlap.
    else {
        p_area = (p_x2 - p_x1)*(p_y2 - p_y1);
        q_area = (q_x2 - q_x1)*(q_y2 - q_y1);

        if(p_x1 < q_x1) {tmp_x1 = q_x1;} else {tmp_x1 = p_x1;}
        if(p_y1 < q_y1) {tmp_y1 = q_y1;} else {tmp_y1 = p_y1;}
        if(p_x2 < q_x2) {tmp_x2 = p_x2;} else {tmp_x2 = q_x2;}
        if(p_y2 < q_y2) {tmp_y2 = p_y2;} else {tmp_y2 = q_y2;}

        area = p_area + q_area - ((tmp_x2 - tmp_x1)*(tmp_y2 - tmp_y1));

        if(p_x2 < q_x2) {tmp_x2 = q_x2;} else {tmp_x2 = p_x2;}
        if(p_x1 < q_x1) {tmp_x1 = p_x1;} else {tmp_x1 = q_x1;}
        if(p_y2 < q_y2) {tmp_y2 = q_y2;} else {tmp_y2 = p_y2;}
        if(p_y1 < q_y1) {tmp_y1 = p_y1;} else {tmp_y1 = q_y1;}
        perimeter = ((tmp_x2 - tmp_x1) + (tmp_y2 - tmp_y1)) * 2;
        // print result.
        cout << area << " " << perimeter << endl;
        continue;
      }

    }
    return 0;


  }
