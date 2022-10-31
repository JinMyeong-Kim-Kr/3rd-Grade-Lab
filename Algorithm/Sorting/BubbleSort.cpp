#include <stdio.h>
#define MAX_SIZE 1000
void bubbleSort(int a[], int n);
void bubbleSortImproved1(int a[], int n);
void bubbleSortImproved2(int a[], int n);
void copyArray(int a[], int b[], int n);
void swap(int* a, int* b);

int main()
{
   int numTestCases;
   scanf("%d", &numTestCases);
   for (int i = 0; i < numTestCases; ++i)
   {
      int num;
      int a[MAX_SIZE], b[MAX_SIZE];
      scanf("%d", &num);

      for (int j = 0; j < num; j++)
         scanf("%d", &b[j]);

      copyArray(a, b, num);
      bubbleSort(a, num);

      copyArray(a, b, num);
      bubbleSortImproved1(a, num);

      copyArray(a, b, num);
      bubbleSortImproved2(a, num);

      printf("\n");
   }
   return 0;
}
/* BubbleSort 함수 */
void bubbleSort(int a[], int n)
{
   int countCmpOps = 0; // 비교 연산자 실행 횟수
   int countSwaps = 0; // swap 함수 실행 횟수
   for (int pass = 0; pass < n ; pass++) {
      for (int i = 1; i < n - pass; i++) {
         countCmpOps += 1;
         if (a[i - 1] > a[i]) {
            countSwaps += 1;
            swap(&a[i - 1], &a[i]);
         }
      }
   }
   printf("%d %d ", countCmpOps, countSwaps);
}
/* BubbleSort 함수 - Improved Version 1 */
void bubbleSortImproved1(int a[], int n)
{
   int countCmpOps = 0; // 비교 연산자 실행 횟수
   int countSwaps = 0; // swap 함수 실행 횟수
   bool swapped;

   for (int pass = 0; pass < n; pass++) {
      swapped = false;
      for (int i = 1; i < n - pass; i++) {
         countCmpOps += 1;
         if (a[i - 1] > a[i]) {
            countSwaps += 1;
            swap(&a[i -1], &a[i]);
            swapped = true;
         }
      }
      if (swapped == false) {
         break;
      }
   }
   printf("%d %d ", countCmpOps, countSwaps);
}

/* BubbleSort 함수 - Improved Version 2 */
void bubbleSortImproved2(int a[], int n)
{
   int countCmpOps = 0; // 비교 연산자 실행 횟수
   int countSwaps = 0; // swap 함수 실행 횟수
   int lastSwapped = n;
   int lastSwappedPos;
   while (lastSwapped > 1) {
      lastSwappedPos = 1;
      for (int i = 1; i < lastSwapped; i++) {
         countCmpOps += 1;
         if (a[i - 1] > a[i]) {
            countSwaps += 1;
            swap(&a[i - 1], &a[i]);
            lastSwappedPos = i;
         }
      }
      lastSwapped = lastSwappedPos;
   }
   printf("%d %d ", countCmpOps, countSwaps);
}
void copyArray(int a[], int b[], int n)
{
   for (int i = 0; i < n; i++)
      a[i] = b[i];
}
void swap(int* a, int* b)
{
   int tmp = *a;
   *a = *b;
   *b = tmp;
}