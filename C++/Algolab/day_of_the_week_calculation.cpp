#include <iostream>
using namespace std;

int CheckLeapYear(int year);
int main(int argc, char const *argv[])
{
    // @numOfTest is the number of test case.
    int numOfTest;
    cin >> numOfTest;

    int year, month, week, day;
    int total_day, first_of_week;

    for(int i = 0; i < numOfTest; i++){
        // 1582 1.1 is friday.
        first_of_week = 5;

        int month_day[] = {31,28,31,30,31,30,31,31,30,31,30,31};
        total_day = 0;
        cin >> year >> month >> day;
        // Check if @year is a leap year.
        int tmp = 1582;
        while(tmp < year){
            // On leap years, the day of the week of January 1 is pushed back twice.
            if (CheckLeapYear(tmp)) first_of_week += 2;
            else first_of_week += 1;
            tmp++;
        }

        // February has 29 days in leap years.
        for(int idx = 0; idx < month - 1; idx++) {
            if(CheckLeapYear(year)) month_day[1] = 29;
            total_day += month_day[idx];
            }
        
        total_day += day - 1;  
        week = ((first_of_week % 7) + total_day) % 7;
        cout << week << endl;
    }

    return 0;
}

// CheckLeapYear checks whether @year is leap year or not.
int CheckLeapYear(int year){
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)){
        return true;
    }
    return false;
}
