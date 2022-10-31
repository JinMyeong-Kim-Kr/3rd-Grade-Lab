#include <iostream>
using namespace std;
#define MAX_SIZE 1000

void combSort(int a[], int n);
void swap(int* a, int* b);

int main()
{
    int numTestCases;
    cin >> numTestCases;

    for(int i = 0; i < numTestCases; ++i){
        int num;
        int a[MAX_SIZE];

        cin >> num;
        for(int j = 0; j < num; j++)
            cin >> a[j];
        combSort(a, num);
        printf("\n");
    }
    return 0;
}

void combSort(int a[], int n){
    int countCmpOps = 0;
    int countSwaps = 0;
    int gap = n;
    float shrink = 1.3;
    bool sorted = false;

    while(!sorted){
        gap /= shrink;
        if(gap <= 1){
            sorted = true;
            gap = 1;
        }
        for(int i = 0; i + gap < n; i++){
            countCmpOps += 1;
            if(a[i] > a[i + gap]){
                countSwaps += 1;
                swap(&a[i], &a[i + gap]);
                sorted = false;
            }
        }
    }
    printf("%d %d ", countCmpOps, countSwaps);
}

void swap(int* a, int* b) { 
    int tmp = *a;
    *a = *b;
    *b = tmp;
    }