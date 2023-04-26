#include <iostream>
using namespace std;
#define MAX_SIZE 1000

void selectionSort(int a[], int n);

int main() {  

    int numTestCases;
    cin >> numTestCases;

    for (int i = 0; i < numTestCases; ++i){        
        int num;         
        int a[MAX_SIZE];

        cin >> num;   
        for (int j = 0; j < num; j++)  
            cin >> a[j];           
    
        selectionSort(a, num);     
    }      
        return 0; 
}  
/* Selection Sort 함수 */ 
void selectionSort(int a[], int n) {    
    int countCmpOps = 0;  // 비교 연산자 실행 횟수     
    int countSwaps = 0;   // swap 함수 실행 횟수     
    int jMin, temp;
    // selection sort 알고리즘 구현       
    for(int i = 0; i < n - 1; i++){
        jMin = i;
        for(int j = i + 1; j < n ; j++){
            countCmpOps += 1;
            if(a[j] < a[jMin]){
                jMin = j;
            }
        }
        if(jMin != i)
            // swap
            countSwaps += 1;
            temp = a[i];
            a[i] = a[jMin];
            a[jMin] = temp; 
    }
    //  printf("%d %d ", countCmpOps, countSwaps); 
    cout << countCmpOps << " " << countSwaps << endl;
} 
 