#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
    int m = 6;
    int n = 4;
    vector<vector<int>> picture = { {1, 1, 1, 0} ,{1, 2, 2, 0},{1, 0, 0, 1},{1, 0, 0, 1},{1, 1, 0, 3},{0, 0, 0, 3} };

    bool v[100][100];

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            v[i][j] = false;
        }
    }


    vector<vector<int>> dir = { {1,0},{0,1},{-1,0},{0,-1} };

    int max_area = 0;
    int part = 0;
    queue<pair<int, int>> q;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] == 0)
                v[i][j] = true;
            else if (v[i][j] == false) {
                part += 1;
                q.push(make_pair(i, j));
                int area = 0;
                int number = picture[i][j];
                while (!q.empty()) {
                    int x = q.front().first;
                    int y = q.front().second;
                    v[x][y] = true;
                    area += 1;
                    cout << x << "   " << y << "   " << part <<  "   " << area << endl;
                    q.pop();
                    for (int k = 0; k < 4; k++) {
                        int dx = x + dir[k][1];
                        int dy = y + dir[k][0];
                        if (dx >= 0 && dy >= 0 && dx < m && dy < n && v[dx][dy] == false && number == picture[dx][dy]) {
                            q.push(make_pair(dx, dy));
                            v[dx][dy] = true;
                        }

                    }
                }
                if (area > max_area)
                    max_area = area;
            }
        }
    }
    cout << part << "    " << max_area << endl;
    return 0;
}

