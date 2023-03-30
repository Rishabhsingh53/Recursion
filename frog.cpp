#include <bits/stdc++.h>
using namespace std;

int frog(int n) {

    if (n < 0) {
        return 0;
    }
    else if (n == 0) {
        return 1;
    }
    return frog(n-1) + frog(n-2);

}

int main() {
    cout << frog(5);
}

