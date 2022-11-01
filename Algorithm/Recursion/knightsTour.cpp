#include <iostream>
#define MARK 1 
#define UNMARK 0 
#define MAXSIZE 9 
using namespace std;
int board[MAXSIZE][MAXSIZE], path[MAXSIZE][MAXSIZE]; 
typedef struct Point {int row, col;} point; 
point direction[8] = {{1, -2}, {2, -1}, {2, 1}, {1, 2}, {-1, 2}, {-2, 1}, {-2, -1} , {-1, -2}};
int knightTour (int m, int n, point pos, int counter)
{
    int i;
    point next;
    if (counter == m * n)
        return 1; 

    for (i = 0; i < 8; i++) { 
        next.row = pos.row + direction[i].row;
        next.col = pos.col + direction[i].col;
        // cout << "next = "<< next.row << " " << next.col << endl;
        if(next.row >= 0 && next.row < m && next.col >= 0 && next.col < n && board[next.row][next.col] != MARK )
        {
            // cout << " true " << endl;
            board[next.row][next.col] = MARK;
            path[next.row][next.col] = counter+1; 
            if ( knightTour(m, n, next, counter+1) )
                return 1;  
            else
                board[next.row][next.col] = UNMARK;
        }
        
    } 
    return 0;
}

int main()
{   
    int i, j, row, col, numOfCase;
    point start;
    cin >> numOfCase;
    for(int c = 0; c < numOfCase; c++){
        cin >> row >> col >> start.row >> start.col;
        // int board[row][col], path[row][col];
        for (i = 0; i < row; i++)
            for (j = 0; j < col; j++)
                board[i][j] = UNMARK;
        start.col -= 1; start.row -= 1;
        board[start.row][start.col] = MARK;
        path[start.row][start.col] = 1; 
        if (knightTour(row, col, start, 1)) {
            cout << 1 << endl;
            for (i = 0; i < row; i++){
                for (j = 0; j < col; j++){
                    cout << path[i][j] << " ";
            }
            cout << endl;
            }
        } 
        else {
            cout << 0 << endl;
            }
    }
    return 0;
}

