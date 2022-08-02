#include <string>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    long long start[5001];
    start[0] = 1;
    start[2] = 3;
    int n = 4;

    for (int i = 4; i <= n; i+=2) {
        start[i] = start[i - 2] * 3;
        for (int j=0; j <= i - 4; j += 2) {
            start[i] += start[j] * 2;
            start[i] %= 1000000007;
        }
    }
}