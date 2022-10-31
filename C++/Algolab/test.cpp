#include <iostream>

using namespace std;

int main(void) {
    unsigned int cases, num, tmp, midVal;
    cin >> cases;

    for (int ca = 0; ca < cases; ca++) {
        cin >> num;

        while (num >= 10) {
            midVal = 1;

            while (num != 0) {
                if (num%10 != 0) {
                    midVal *= num%10;
                }
                num /= 10;
            }

            num = midVal;
        }

        cout << num << endl;
    }
}
