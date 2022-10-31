#include <iostream>
using namespace std;
#define MAX_SIZE 1000

void insertionSort(int a[], int n);

int main(){
    int numTestCases;
    cin >> numTestCases;

    for(int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];

        cin >> num;
        for(int j = 0; j < num; j++)
            cin >> a[j];
        
        insertionSort(a, num);
    }
}

void insertionSort(int a[], int n){
    int countCmpOps = 0;
    int countSwaps = 0;
    int temp;
    for(int i = 1; i < n; i++){
        for(int j = i; j > 0; j--){
            countCmpOps += 1;
            if(a[j - 1] > a[j])
            {
                countSwaps += 1;
                // swap
                temp = a[j-1];
                a[j-1] = a[j];
                a[j] = temp;
            }
            else{
                break;
            }
        }
    }
    cout << countCmpOps << " " << countSwaps << endl;
}