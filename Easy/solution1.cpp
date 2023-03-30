#include <bits/stdc++.h>
using namespace std;

// print five times hello world

void message(int n) {
    if (n == 0) {
        return;
    }
    cout << " Hello World! " << endl;
    message(n-1);
}

int main() {
    message(5);
}
