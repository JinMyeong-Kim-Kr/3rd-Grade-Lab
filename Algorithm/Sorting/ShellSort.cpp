#include <iostream>
using namespace std;
#define MAX_SIZE 1000

void shellSort(int a[], int n);
void swap(int* a, int* b);

int main(){
    int numTestCases;
    cin >> numTestCases;

    for(int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];

        cin >> num;
        for(int j = 0; j < num; j++)
            cin >> a[j];
        
        shellSort(a, num);
    }
}

void shellSort(int a[], int n){
    int countCmpOps = 0;
    int countSwaps = 0;
    int shrinkRatio = 2;
    int gap = n / shrinkRatio;
    int tmp;
    while (gap > 0){
        for(int i = gap; i < n; i++){
            for(int j = i; j >= gap; j -= gap){
                countCmpOps += 1;
                if(a[j - gap] > a[j]){
                    countSwaps += 1;
                    // swap
                    tmp = a[j - gap];
                    a[j - gap] = a[j];
                    a[j] = tmp;
                }
                else{
                    break;
                }
            }
        }
        gap /= shrinkRatio;
    }
    cout << countCmpOps << " " << countSwaps << endl;

}
